#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#from download import *
import urllib2
import urllib
import re
import os
import datetime
import random
import lxml

default_dir     = "D:/python/save/ershoufang/"
default_agetnt  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063';
default_url     = "https://bj.lianjia.com/ershoufang/"
link_reg        = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
content_reg     = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
domain          = "https://bj.lianjia.com"


def download(url,dir=dir,name=None):

    #生成默认的名称
    if name == None:
        defaultName = urllib2.urlparse.urlparse(url).path.split('/')[-1];
    else:
        defaultName = name;

    #生成路径
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir);

    #拼接路径
    path = os.path.join(dir, defaultName);

    #下载
    urllib.urlretrieve(url, path);

    #hint
    print "文件%s下载成功" % path;

#从html页面中获取所有的链接
def get_link(html):
    link_reg = '<a[^>]+href=["\'](.*?)["\']' 
    reg_obj = re.compile(link_reg,re.IGNORECASE);
    return reg_obj.findall(html);


def lxml(html):
    pass;

def link_filter(url, reg):

    html = curl(url, 2)

    for link in get_link(html):
        if re.match(reg, link):
            print link;

def lianjia_craw():
    z = 1
    crawer_content_seen = set([]);
    for i in range(1,10000):
        print i;
        html = curl("https://bj.lianjia.com/ershoufang/pg%d" % i,2);
        for link in get_link(html):
            if re.match(content_reg, link):
                if link not in crawer_content_seen:
                    crawer_content_seen.add(link);
                    print z, link;
                    z = z+1;
                else:
                    pass;
            else:
                pass;

def link_crawer(url, c_reg, l_reg):
    crawer_queue = [url];
    crawer_content_seen = set([]);
    crawer_link         = set(crawer_queue);
    crawer_link_seen    = set([]);

    while crawer_link:
        url = crawer_link.pop()
        html = curl(url, 2)

        for link in get_link(html):
            if re.match(c_reg, link):
                if link not in crawer_content_seen:
                    crawer_content_seen.add(link);
                    #print link;
            elif re.match(l_reg, link):
                link_all = urllib2.urlparse.urljoin(domain, link);
                print link_all
                continue;
                if link_all not in crawer_link_seen: 
                    crawer_link_seen.add(link_all);
                    crawer_link.add(link_all);
                    print link_all;
                else:
                    pass;
            else:
                pass;


  #              link = urllib2.urlparse.urljoin(url, link);
  #             if link not in crawer_seen:
  #                 crawer_seen.add(link);
  #                 crawer_queue.insert(0, link);
   

def curl(url, num_retry , type = None, user_agent = default_agetnt, proxy = None, data = None):
    #print "download url:", url
    headers = {'User-agent':user_agent};
    request = urllib2.Request(url, data, headers=headers);

    while num_retry > 0:

        try:
            html=  urllib2.urlopen(request).read();
            host = urllib2.urlparse.urlparse(url).netloc.split('.');
            break;
        except urllib2.URLError as e:
            print num_retry,'Download error:',e
            if hasattr(e,'code') and  600 > e.code >= 320:
                print("lalalal");
            html = None;
            num_retry = num_retry - 1;
    return html;

def main(url):
    link_crawer(url,link_reg,'/ershoufang/pg[0-9]+/');





lianjia_craw();