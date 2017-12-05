#!/usr/local/bin/python

import time, threading

def loop():
	i = 0;
	while i < 5:
		i = i+1;
		print("% running %d" % (threading.current_thread().name, i));
		time.sleep(1);

	print("% running " % (threading.current_thread().name));


t = threading.Thread(target=loop, name="hah");

t.start();
t.join();

print("% running" % threading.current_thread().name);
