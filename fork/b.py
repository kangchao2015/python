#!/usr/local/bin/python
from multiprocessing import Process, Queue
import os, time, random


def write(q):
	for i in range(1,100):
		print("Process %d write %s" % (os.getpid(), i));
		q.put(i);
		time.sleep(random.random());


def read(q):
	while True:
		value = q.get(True);
		print("Process %d get %s" % (os.getpid(), value));


if __name__ == '__main__':


	q = Queue();
	pw = Process(target=write, args = (q,));
	pr = Process(target=read, args = (q,));

	pw.start();
	pr.start();


	pw.join();
		
