#/usr/local/bin/python


a = list(range(10));

print(a);
#print[x * 2 + 10 for x in a];
b = map(lambda x:x*2 + 10, a);
for z in b:
	print(z);

exit(1);



def _odd_iter():
	n = 1;
	while True:
		n = n+1;
		yield n;


def _nod_divi(n):
	return lambda x:x % n > 0;

def hahah():
	yield 2
	it = _odd_iter();
	while True:
		n = next(it);
		yield n;
		it = filter(_nod_divi(n), it);

k = int(input("input:"));

for n in hahah():
	if n > k:
		print (n);
	else:
		continue;
