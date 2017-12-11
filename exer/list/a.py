#!/usr/local/bin/python
import os

a={'a':'asdf', 'b':'zzz', 'c':'qqq'}

print([x * x for x in range(1,100) if x % 9 == 1]);
print([x + n for x in 'kangchao' for n in 'loveyou' ]);
print([d for d in os.listdir('.')]);
print([a+':'+b for a, b in a.items()]);

g = (x * x for x in range(10));


for i in g:
	print(i);

for k, v in a.items():
	print(k+v);

