#!/usr/local/bin/python
# -*- coding:utf-8 -*-
from download import *
import urllib2
import re
import os
import datetime
import random



def download(url):
    try:
        html=  urllib2.urlopen(url).read();
    except urllib2.URLError as e:
        print 'Download error:', e
        html = None;
    return html;


def download2(url, num_retry, name = None ,user_agent = 'test', proxy = None, data = None):
#    os.mkdir("site", 0777);
    print "download url:", url

    headers = {'User-agent':user_agent};
    request = urllib2.Request(url, data, headers=headers);

    while num_retry > 0:

        try:
            html=  urllib2.urlopen(request).read();
            host = urllib2.urlparse.urlparse(url).netloc.split('.')[1];
            if name == None:
                n = host
            else:
                n = name;
            with open("./site/%s_%s.html" % (n , random.randint(0,100000)),"w") as w:
                pass
              #   w.write(html); 
            break;
        except urllib2.URLError as e:
            print num_retry,'Download error:',e
            if hasattr(e,'code') and  600 > e.code >= 320:
                print("lalalal");
            html = None;
            num_retry = num_retry - 1;

    return html;

def download3(url):
    print "download url:", url
    
    html=  urllib2.urlopen(url);
    print dir(html);
    print "==================================";
    print "geturl:",html.geturl();    #
    print "==================================";
    print "headers:",html.headers;
    print "==================================";
    print "info",html.info();
    print "==================================";
    print "getcode:",html.getcode();

def get_link(html):
    link_reg = '<a[^>]+href=["\'](.*?)["\']' 
    reg_obj = re.compile(link_reg,re.IGNORECASE);
    return reg_obj.findall(html);

def link_crawer(url, reg):
    crawer_queue = [url];
    crawer_seen = set(crawer_queue);

    while crawer_queue:
#        for i in crawer_queue:
#            print "queue:",i;
        url = crawer_queue.pop()
        html = download2(url, 2)
        for link in get_link(html):
            if re.match(reg, link):
                link = urllib2.urlparse.urljoin(url, link);
                if link not in crawer_seen:
                    crawer_seen.add(link);
#                    print "join url:", link
                    crawer_queue.insert(0, link);
   



url = "http://www.baidu.com"
#url = "http://www.qq.com"
url = "http://www.bladeblue.top"
url = "http://www.qiushibaike.com"
#while n < 600:
#    web = "%s%d" % (url, n)
#/8hr/page/2/
#info = download2(url,2, 'mobile', user_agent = 'User-Agent:Mozilla/5.0 (Linux; U; Android 4.1; en-us; GT-N7100 Build/JRO03C) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30');
#info = download2(url,2, 'pc', user_agent = 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14')
#html = download2(url, 2);
#info = get_link(html);
#print(info);
link_crawer(url, "(/8hr/page/[0-9]+)|/article/[0-9]+");


