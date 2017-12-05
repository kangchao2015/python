#/usr/local/bin/python


a = [x*y for x in range(1,10) for y in range(11,20)]
b = (x*y for x in range(1,10) for y in range(11,20))

#while True:
#	print(next(b));


#for i in b:
#	print(i);

exit(-1);

def fib(max):
	for x in range(1,max):
		for y in range(11,20):
			yield x*y;

#print(fib);
L = [];
for i in fib(100):
	L.append(i);
print(L);
pp = oct
print(pp);



abs=10;
abs(-10);
