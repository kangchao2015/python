#!/usr/local/bin/python
# -*- coding:utf-8 -*-
#from download import *
import urllib2
import urllib
import re
import os
import datetime
import random

dir = '.';
ud2 = "http://i1.cache6.us/1100/201712/04/l4kj55bgsl0.jpg";
url3 = "http://www.bladeblue.top/wp-content/uploads/2017/07/Linux-OS-Logo_1920x1080_60521.jpg"

def download(url, path):
    path = os.path.join('.',"a.jpg");
    print path;
    urllib.urlretrieve(url, path);


def save(dir,name,info):
    if os.path.exists(dir):
        pass
    else:
        os.mkdir(dir);
    path = os.path.join(dir,name);
    
    with open(path, "w") as e:
        e.write(info);

#type = 0 表示 是列表页
#type = 1 表示 是详情页
def curl(url, num_retry , type, user_agent = 'test', proxy = None, data = None):
#    os.mkdir("site", 0777);
    print "download url:", url

    headers = {'User-agent':user_agent};
    request = urllib2.Request(url, data, headers=headers);

    while num_retry > 0:

        try:
            html=  urllib2.urlopen(request).read();
            host = urllib2.urlparse.urlparse(url).netloc.split('.');
  
    #        name = "host[0]_%s"
        
            break;
        except urllib2.URLError as e:
            print num_retry,'Download error:',e
            if hasattr(e,'code') and  600 > e.code >= 320:
                print("lalalal");
            html = None;
            num_retry = num_retry - 1;

    return html;

def get_link(html):
    link_reg = '<a[^>]+href=["\'](.*?)["\']' 
    reg_obj = re.compile(link_reg,re.IGNORECASE);
    return reg_obj.findall(html);

def link_crawer(url, reg, max_depth = -1):
    crawer_queue = [url];
    crawer_seen = set(crawer_queue);

    while crawer_queue:
#        for i in crawer_queue:
#            print "queue:",i;
        url = crawer_queue.pop()
        html = curl(url, 2)

        for link in get_link(html):
            if re.match(reg, link):
                link = urllib2.urlparse.urljoin(url, link);
                if link not in crawer_seen:
                    crawer_seen.add(link);
#                    print "join url:", link
                    crawer_queue.insert(0, link);
   



#info = curl(url,2, 1, user_agent = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063')
download(ud2, dir)
