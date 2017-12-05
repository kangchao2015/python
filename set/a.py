#!/usr/local/bin/python




a = set([1,2,3,4,1,2,3,4]);
b = set([1,2,3,4,1,2,3,4]);

b.add('asdf');
a.remove(3);


b.add([1,2,3]);

c = a | b

print(c);
