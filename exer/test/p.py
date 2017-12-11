#!/usr/local/bin/python




def my_dis(a,b):
	for i in a:
		print(i);
	print(b);
	print("---------------------")

	lo = 0;
	lo = b % len(a);

	print(lo);

	while len(a) != 0:
		print(len(a));
		pass


def main():

	aa = [x for x in range(10)]
	bb = 5;
	
	my_dis(aa,bb);


main();
	
