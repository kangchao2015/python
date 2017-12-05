#!/usr/local/bin/python

from multiprocessing import Process, Queue
import os
import subprocess
import time, random,os


for i in dir(Process):
	print("--%s" % i);


exit(-1);
r = subprocess.call(['nslookup', 'www.baidu.com']);
print("%d" % r);

exit(-1);







pid = os.fork();
if pid == 0:
	print("child process %d\n" % os.getpid());
else:
	print("father process %d\n" % os.getpid());




