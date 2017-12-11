# -*- coding:utf-8 -*-
#from download import *
import urllib2
import urllib
import re
import os
import datetime
import random
from lxml import etree

default_dir     = "D:/python/save/ershoufang/"
default_agetnt  = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063';
default_url     = "https://bj.lianjia.com/ershoufang/"
default_links   = "https://bj.lianjia.com/ershoufang/dongcheng/";

link_reg        = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
content_reg     = "https://bj.lianjia.com/ershoufang/[0-9]+.html"
domain          = "https://bj.lianjia.com"

#已经爬取过的页面集合
crawer_content_seen = set([]);
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

def download(url,dir=dir,name=None):

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
    print "文件%s下载成功" % path;

def get_all_link(html):
    link_reg = '<a[^>]+href=["\'](.*?)["\']' 
    reg_obj = re.compile(link_reg,re.IGNORECASE);
    return reg_obj.findall(html);

def lianjia_craw(url):
    print url;
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
                    print z,link;
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
        
        if os.path.exists(os.path.join(dir,name)):
            pass;
        else:
            os.mkdir(os.path.join(dir,name));
        dir = os.path.join(dir,name);
        domain_local = "https://%s" % urllib2.urlparse.urlparse(url).netloc

        for j  in get_distract(url,1):
            sub_url = j.attrib['href'];
            sub_name = j.text;
            if re.match("^https", sub_url):
                pass;
            else:
                sub_url = urllib2.urlparse.urljoin(domain_local, sub_url); 

            if os.path.exists(os.path.join(dir,sub_name)):
                pass;
            else:
                sub_dir = os.path.join(dir,sub_name);
                os.mkdir(sub_dir);
                print sub_dir;

            lianjia_craw(sub_url)



main(default_links);