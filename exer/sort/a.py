#!/usr/local/bin/python



L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
a = [1,-20,-3,4,5]
s = ['kang','chao','Zk'];


print(sorted(a, key = abs));
print(sorted(s, key=str.lower));


def aa(a):
	return a[1];

print(sorted(L, key=aa));
print(sorted(L, key=lambda x:x[0]));
