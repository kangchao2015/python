#/usr/local/bin/python
# -*- coding: utf-8 -*-
' a test module '

__author__ = 'Michael Liao'


import sys

def kkk():
	args = sys.argv
	if len(args) == 1:
		print("aaaaaaa");
	elif len(args) == 2:
		print("bbbbbbb");
	else:
		print("ccccccccccc");

if __name__=='__main__':
    kkk()
