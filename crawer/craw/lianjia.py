#-*-coding:utf-8 -*-

#from download import *
import urllib2
import urllib
import re
import os
import datetime
import random
import codecs
from lxml import etree
import sys
import csv
reload(sys)
sys.setdefaultencoding('utf8');

default_dir     = "D:/python/save/ershoufang/"
default_agetnt  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063';
default_url     = "https://bj.lianjia.com/ershoufang/"
default_links   = "https://bj.lianjia.com/ershoufang/dongcheng/";

link_reg        = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
content_reg     = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
domain          = "https://bj.lianjia.com"

p1 = "";
p2 = "";
bom = 0;
total = 0;

#已经爬取过的页面集合
crawer_content_seen = set([]);
info_count = {};
z =1;

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

def download(url,dir,name=None):

    if name == None:
        defaultName = urllib2.urlparse.urlparse(url).path.split('/')[-1];
    else:
        defaultName = name;

    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir);
    path = os.path.join(dir, defaultName); 

    urllib.urlretrieve(url, path);
#    print "文件%s下载成功" % path;

def get_all_link(html):
    link_reg = '<a[^>]+href=["\'](.*?)["\']' 
    reg_obj = re.compile(link_reg,re.IGNORECASE);
    return reg_obj.findall(html);

def get_content_page(url):

    global p1, p2, bom,total;
    html = curl(url,2);
    info = [];
    inl = ["____厅室",'____楼层','____朝向','____装修','____大小','____年代'];
    info_name = [];
    #去掉非法字符
    for zz in inl:
        info_name.append(zz.decode('utf-8', 'ignore'))

    page = etree.HTML(html.lower().decode('utf-8'));
    restult = {};

    try:
        node_title      = page.xpath(u"//h1[@class='main']")[0];
        node_total      = page.xpath(u"//span[@class='total']")[0];
        node_price      = page.xpath(u"//span[@class='unitpricevalue']")[0];
        node_houseinfo  = page.xpath(u"//div[@class='houseinfo']")[0];
        node_around     = page.xpath(u"//div[@class='aroundinfo']")[0];
        node_basic      = page.xpath(u"//div[@class='introcontent']")[0];
        node_charac     = page.xpath(u"//div[@class='introcontent showbasemore']")[0];
        node_pic        = page.xpath(u"//div[@class='content-wrapper housepic']")[0];

        #添加houseinfo 到result中
        for sub_houseinfo in node_houseinfo:
            for sub_sub_houseinfo  in sub_houseinfo:
                info.append(sub_sub_houseinfo.text);

        d =  dict(zip(info_name, info));
        for i,j in d.items():
            restult[i] = j

        #aroundinfo 到result中
        i = 1;
        for sub_around in node_around:
            
            if i == 1:
                s_l = sub_around.xpath("span")[0].text;
                s_n = sub_around.xpath("a")[0].text;
                restult[s_l] = s_n;
            elif i == 2:
                s_l = sub_around.xpath("span")[0].text;
                s_n1 = sub_around.xpath("span/a")[0].text;
                s_n2 = sub_around.xpath("span/a")[1].text;
                restult[s_l] = "%s %s" % (s_n1, s_n2);
            elif i == 3 or i ==4:
                s_l = sub_around.xpath("span")[0].text;
                s_n = sub_around.xpath("span")[1].text;
                restult[s_l] = s_n;
            else:
                pass;
            i = i +1;

        #basic 添加到result中
        l  = ['base','transaction'];
        for ol in l:
            for sub_basic in node_basic.xpath("div[@class='%s']/div[@class='content']/ul" % ol)[0]:
                sl = sub_basic.xpath('span')[0].text;
                if len(sub_basic.xpath('span')) == 2:
                    sn = sub_basic.xpath('span')[1].text;
                else:
                    sn = sub_basic.xpath('span')[0].tail;

                restult[sl] = sn;

        #添加charac 搭配restult中
        for sub_charac in node_charac:
            if sub_charac.attrib["class"] in {"baseattribute clear","tags clear"}:
                sl = sub_charac.xpath('div')[0].text.strip();
                sn = sub_charac.xpath('div')[1].text.strip();
                if sn == "":
                    for ssn in sub_charac.xpath('div')[1].getchildren():
                        sn = "%s %s" % (sn,ssn.text);
            else:
                continue;
            restult[sl] = sn;

        #单条信息添加
        restult['____标题'.decode('utf-8','ignore')]  =  node_title.text;
        restult['____总价'.decode('utf-8','ignore')]  =  node_total.text;
        restult['____单价'.decode('utf-8','ignore')]  =  node_price.text;

        
        #下载图片
        xiaoqu =  restult['小区名称'.decode('utf-8','ignore')];
        if  xiaoqu not in info_count:
            info_count[xiaoqu] = 1;
        else:
            info_count[xiaoqu] = info_count[xiaoqu] + 1;

    #    print default_dir,p1, p2,xiaoqu, info_count[xiaoqu];
        xpath    = os.path.join(default_dir, p1, p2,xiaoqu, "%d" % info_count[xiaoqu]);
        rpath    = xpath.split('/');
        dz = ""
        q = 0;
        for r in rpath:
            if q<3:
                q = q+1;
                continue;
            dz = "%s/%s" % (dz, r)

        restult["____图片".decode('utf8')] = dz;
        


        xpath = xpath.replace('\\','/');
        if os.path.exists(xpath):
            pass;
        else:
            os.makedirs(xpath.decode('utf8'));

        imgs = node_pic.xpath(".//img[@src]");
        p = 1;
        for img in imgs:
            src = img.attrib['src'];
            tail = os.path.splitext(src)[1];
            download(src,xpath.decode('utf8'),name = "%d%s" % (p,tail));
            p = p + 1;
        print xpath," %d images download done!" % p;

#    colums = ['指针','的']
        colums = ['链家编号','小区名称','____大小','____标题','____楼层','____图片','____总价','____朝向','____装修','____厅室','____单价','____年代','交通出行','挂牌时间','所在楼层','户型结构','套内面积','房屋用途','装修情况','配备电梯','产权年限','建筑类型','交易权属','梯户比例','看房时间','产权所属','建筑结构','供暖方式','房屋年限','税费解析','上次交易','所在区域','小区介绍','房屋朝向','房本备件','房屋户型','权属抵押','抵押信息','建筑面积','核心卖点','房源标签'];
        colums_utf8 = [];
        for gg in colums:
            colums_utf8.append(gg.decode('utf8','ignore'));

        with open(default_dir+"a.csv", "ab") as q:
            if bom == 0:
                q.write(codecs.BOM_UTF8)
                for dda in colums:
                    q.write(dda + ',');
                q.write("\r\n");
                bom = 1;

        with open(default_dir+"a.csv", "ab") as q:
            str = "";
            for item in colums:
                for i,j in restult.items():
                    kk = ","
                    if item == i:
                        j = j.replace(',',' ');
                        kk = "%s%s" % (j, ",");
                        break;

                str = str + kk;
            q.write(str + "\r\n");


        total = total + 1;
        if '链家编号'.decode('utf8','ignore') in restult:
            print "%s %d done\n" % (restult['链家编号'.decode('utf8','ignore')],total);
        else:
            print total;
    except Exception as e:
        with open(default_dir+"err.txt", "ab") as v:
            if '链家编号'.decode('utf8','ignore') in restult:
                v.write("%s,%s" % (restult['链家编号'.decode('utf8','ignore')], e));

def lianjia_craw(url):
    global crawer_content_seen;
    global z;

    for i in range(1,200):
        #print i;
        j = 0;
        html = curl("%spg%d" % (url,i),2);
        reo = re.compile(content_reg, re.IGNORECASE);

        for link in get_all_link(html):

            if re.match(content_reg, link):
                if link not in crawer_content_seen:
                    crawer_content_seen.add(link);
                    get_content_page(link);
                    z = z+1;
                    j = j+1
                else:
                    pass;
            else:
                pass;  

        if j == 0:
            break;
        



def get_distract(link,way=0):
    html = curl(link,2);

    page = etree.HTML(html.lower().decode('utf-8'))
    parent = page.xpath(u"//div[@data-role='ershoufang']")[0];

    if way == 0:
        return parent.getchildren()[0].getchildren();
    else:
        return parent.getchildren()[1].cssselect("a");


def main(url,dir = default_dir):

    global p1;
    global p2;

    if os.path.exists(dir):
        pass;
    else:
        os.mkdir(dir);

    for i in get_distract(url,0):
        dir = default_dir;
        url = i.attrib['href']
        name =  i.text;
        if re.match("^https", url):
            pass;
        else:
            url = urllib2.urlparse.urljoin(domain, url); 
        p1 = name;
        if os.path.exists(os.path.join(dir,name)):
            pass;
        else:
            os.mkdir(os.path.join(dir,name));
            p1 = name;
        dir = os.path.join(dir,name);
        domain_local = "https://%s" % urllib2.urlparse.urlparse(url).netloc

        for j  in get_distract(url,1):
            sub_url = j.attrib['href'];
            sub_name = j.text;
            if re.match("^https", sub_url):
                pass;
            else:
                sub_url = urllib2.urlparse.urljoin(domain_local, sub_url); 

            p2 =sub_name;
            if os.path.exists(os.path.join(dir,sub_name)):
                pass;
            else:
                sub_dir = os.path.join(dir,sub_name);
                p2 = sub_name;
                os.mkdir(sub_dir);
                print sub_dir;

            lianjia_craw(sub_url)



main(default_links);

get_content_page("https://bj.lianjia.com/ershoufang/101102223096.html");