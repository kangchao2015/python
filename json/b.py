#!/usr/local/bin/python
import json



class a():

	def __init__(self, name):
		self.name = name;	



aa = a("kangchao");



jsona = json.dumps((aa) , default=lambda obj:obj.__dict__);



