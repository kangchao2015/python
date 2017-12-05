#!/usr/local/bin/python


import urllib.request

url = "http:www.baidu.com"
data = urllib.request.urlopen(url).read();
date = data.decode('UTF-8');
print(data);
