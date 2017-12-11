#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基于https://github.com/fancyspeed/sf-extractor/blob/master/sf_extractor.py修改

import chardet
import re
import requests

FLAG = re.I|re.M|re.S|re.U

LINKMARK = '|LINKMARK|' # 用于标记页面中的链接
IMAGEMARK = '|IMAGEMARK|' # 用于标记页面中的图片

PUNCS = re.compile(r'[^\s\w]', FLAG) # 页面中的标点
FOOTER = re.compile(r'备\d+号|Copyright\s*©|版权所有|all rights reserved|广告|推广|回复|评论|关于我们|链接|About|广告|下载|href=|本网|言论|内容合作|法律法规|原创|许可证|营业执照|合作伙伴|备案', FLAG) # 页面页脚文字
TITLE = re.compile(r'<(?:h1|title)[^>]*?>(.*?)</(?:h1|title)>', FLAG) # 页面标题
TAGS = re.compile(r'<[^>]*?>', FLAG) # 页面中的标签

PRESUB = (
    (re.compile(r'<(?:\?|script|style)[^>]*?>.*?</(?:\?|script|style)>', FLAG), ''), # 清除页面中的php、js和css
    (re.compile(r'<!--\s*?\[.*?\]\s*?-->', FLAG), ''), # 清除页面中成对的注释标签及包含的内容（例如浏览器判断）
    (re.compile(r'&quot;|&#34;', FLAG), '"'),
    (re.compile(r'&amp;|&#38;', FLAG), '&'),
    (re.compile(r'&lt;|&#60;', FLAG), '<'),
    (re.compile(r'&gt;|&#62;', FLAG), '>'),
    (re.compile(r'(?:&nbsp;|&#160;|&\w{2,6};|&#\w{2,5};|\f|\s|\t|\v)+', FLAG), ' '), # 将连续的空格替换为单空格
    (re.compile(r'<a[^>]*?>|</a>', FLAG), LINKMARK), # 标记所有的链接标签
    (re.compile(r'<img[^>]*?>', FLAG), IMAGEMARK) # 标记所有的图片标签
)

class Article(object):

    __slots__ = ('content', 'title')

    @property
    def overview(self):
        total_words = len(self.content)
        show_words = total_words // 10
        hidden_words = total_words - show_words

        return '标题：{title}\n正文：{content}……\n\n还有{words}字'.format(
            title = self.title,
            content = self.content[:show_words],
            words = hidden_words
        )

    @property
    def text(self):
        return '\n\n'.join((self.title, self.content))

    @property
    def markdown(self):
        return '\n'.join(('# ' + self.title, self.content)).replace('\n', '\n\n')

    @property
    def html(self):
        return '<html>\n<head>\n<title>{title}</title>\n<style>\n{style}\n</style>\n</head>\n<body>\n<h1>{head}</h1>\n{content}</body>\n</html>'.format(
            title = self.title,
            style = 'h1 {\nfont-size: 32px;\nline-height: 58px;\ntext-align: center;\n}\np {\nfont-size: 16px;\nline-height: 34px;\ntext-align: left;\ntext-indent: 2em;\n}',
            head = self.title,
            content = ''.join('<p>{}</p>\n'.format(line) for line in self.content.splitlines())
        )

    def save(self, ext, data):
        # 将文章标题作为保存的文件名，将标题中不能作为文件名的特殊字符替换为下划线
        filename = '.'.join((re.sub(r'\\|\/|\:|\*|\?|\"|\'|\<|\>|\|', '_', self.title), ext))

        with open(filename, 'w', errors='ignore') as f:
            f.write(data)

    def save_text(self):
        self.save('txt', self.text)

    def save_markdown(self):
        self.save('md', self.markdown)

    def save_html(self):
        self.save('html', self.html)

class Extractor(object):

    __slots__ = ('threshold',)

    def __init__(self, threshold=10):
        self.threshold = threshold

    def get_document(self, url):
        try:
            if re.match('^https?\:\/\/.+', url):
                resp = requests.get(url)
                if resp.status_code != 200: raise
                buf = resp.content
                resp.close()
            else:
                with open(url, 'rb') as f:
                    buf = f.read()

            enc = chardet.detect(buf)['encoding']

            if enc is None: raise
            elif enc == 'GB2312': enc = 'gbk' # 对于简体中文，选择兼容性更好的GBK编码
        except:
            document = url
        else:
            document = buf.decode(enc)

        for reg, rep in PRESUB:
            document = reg.sub(rep, document)

        return document.strip()

    def get_blocks(self, lines):
        if len(lines) == 0: return []

        line_words = [len(line) for line in lines]
        line_count = len(lines)

        empty_blocks = []
        start_idx = 0

        for end_idx in range(0, line_count):
            if line_words[end_idx] != 0 and end_idx > start_idx:
                empty_blocks.append(end_idx - start_idx - 1)
                start_idx = end_idx

            if end_idx == line_count - 1 and end_idx > start_idx:
                empty_blocks.append(end_idx - start_idx - 1)

        if len(empty_blocks) == 0 : return []

        sorted_list = []

        for v in sorted(empty_blocks):
            sorted_list.extend([v] * v) if v > 1 else sorted_list.append(v)

        prop_interval = max(3, sorted_list[len(sorted_list) // 5] + 1)

        blocks = []
        start_idx = 0

        for end_idx in range(0, line_count):
            if sum(line_words[end_idx:end_idx+prop_interval]) <= 3 and end_idx > start_idx:
                if sum(line_words[start_idx:end_idx]) >= self.threshold:
                    blocks.append((start_idx, end_idx))

                start_idx = end_idx + prop_interval

                while start_idx < line_count - 1 and line_words[start_idx] <= 2:
                    start_idx += 1

            if end_idx == line_count - 1:
                if sum(line_words[start_idx:end_idx]) >= self.threshold:
                    blocks.append((start_idx, end_idx))

        return blocks

    def stat_blocks(self, lines, blocks):
        line_count = len(lines)

        block_scores = []

        for start_idx, end_idx in blocks:
            block = '\n'.join(lines[start_idx:end_idx])
            line_num = end_idx - start_idx + 1
            clean_block = block.replace(LINKMARK, '')

            position_rate = (line_count - start_idx + 1) / (line_count + 1)
            document_density = (len(clean_block) + 1) / line_num

            image_density = (block.count(IMAGEMARK) + 1) / line_num # 加分项：图片密度
            punc_density = (len(PUNCS.findall(clean_block)) + 1) / line_num # 加分项：标点密度
            link_density = (block.count(LINKMARK) + 1) / line_num # 减分项：链接密度
            footer_density = (len(FOOTER.findall(clean_block)) + 1) / line_num # 减分项：页脚密度

            block_scores.append(position_rate * document_density * image_density * pow(punc_density, 0.5) / link_density / pow(footer_density, 0.5))

        return block_scores

    def extract_title(self, document):
        try: return re.split(r'\-|\||_', TITLE.findall(document)[0])[0]
        except: return '无标题'

    def extract_content(self, document):
        lines = [line.strip() for line in document.splitlines()]
        blocks = self.get_blocks(lines)
        if len(blocks) == 0: return ''

        block_scores = self.stat_blocks(lines, blocks)
        best_idx, best_block, best_score = -1, None, max(block_scores) - 1

        for idx, score in enumerate(block_scores):
            if score > best_score:
                best_idx = idx
                best_block = blocks[idx]
                best_score = score

        idx = best_idx - 1

        while idx >= 0:
            new_block = blocks[idx][0], best_block[1]
            new_score = self.stat_blocks(lines, [new_block])[0]

            if new_score > best_score:
                best_score = new_score
                best_block = new_block
                idx -= 1
            else:
                break

        idx = best_idx + 1

        while idx < len(blocks):
            new_block = best_block[0], blocks[idx][1]
            new_score = self.stat_blocks(lines, [new_block])[0]

            if new_score > best_score:
                best_score = new_score
                best_block = new_block
                idx += 1
            else:
                break

        return '\n'.join((line for line in lines[best_block[0]:best_block[1]] if len(line) > 0)).replace(LINKMARK, '').replace(IMAGEMARK, '')

    def extract(self, url):
        document = self.get_document(url)
        article = Article()

        if len(document) > 0:
            article.title = self.extract_title(document)
            document = TAGS.sub('\n', document) # 在获取标题之后，去除掉页面中的全部标签
            article.content = self.extract_content(document)
        else:
            article.title, article.content = '', ''

        return article

