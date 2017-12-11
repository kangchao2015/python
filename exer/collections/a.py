#!/usr/local/bin/python

t = (1,2,3,4,5);
l = ['namg', 'sex', '1123', False, 1];
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
s = set(t);


for i in d:
	print(i);

for i in d.values():
	print(i);

for i,j in d.items():
	print(i,'+',j);
