#!/usr/local/bin/python
import os;
import time;


def my_dis(a):
	for i in a:
		print(i);
	print("---------------------")

def odd():
    print('step 1')
    time.sleep(1);
    yield 1
    time.sleep(1);
    print('step 2')
    time.sleep(1);
    yield(3)
    time.sleep(1);
    print('step 3')
    time.sleep(1);
    yield(5)

def main():

	aa = ["%d * %d" % (x,x) for x in range(1,100) if x % 2 ==0]
	bb = ["%d * %d" % (x,y) for x in range(1,10) for y in range(11,20) if x % 3 ==0]
	cc = [d for d in os.listdir('../')];
#	dd = [x for x in range(1,100000000)];




#	my_dis(dd);


main();
	
