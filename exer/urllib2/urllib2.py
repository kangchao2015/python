#!/usr/local/bin/python3


import urllib2

url = "http://www.baidu.com"
data = urllib2.urlopen(url).read();
date = data.decode('UTF-8');
print(data);
