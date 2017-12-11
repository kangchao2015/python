#!/usr/local/bin/python
import urllib2





url = "http://www.baidu.com/123.html"


ret = urllib2.urlparse.urlparse(url)
#host = ret['netloc']
print type(ret)
print dir(ret)
host = ret.netloc
print host.split('.')[1];

exit(-1);
