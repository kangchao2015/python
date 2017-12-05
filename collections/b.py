#/usr/local/bin/python

from collections import namedtuple

_p = (2,3,4);

p = namedtuple('corrdents', ['x','y']);
p1 = p(1,2);
print(p1.x, p1.y);

