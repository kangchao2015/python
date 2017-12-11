#!/usr/local/bin/python

class man(object):
	def say(self):
		print("this is a man saying...");	

class hihi(man):
	pass

class Student(man):
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender
	
	def get_name(self):
		return self.__name;

	def get_gender(self):
		return self.__gender;
	
	def set_name(self, name):
		self.__name = name;

	def set_gender(self, gender):
		if((gender == 'male') | (gender == 'female')):
			self.__gender = gender;


k = Student("kangchao", "male");
print("%s %s" % (k.get_name(), k.get_gender()));
k.set_gender("female")
print("%s %s" % (k.get_name(), k.get_gender()));
print("%s %s" % (k._Student__name, k._Student__gender));

h = hihi();
h.say();


print(isinstance(h, object));
print(isinstance(h, Student));
print(isinstance(h, list));
print("\n %s" % dir(Student));
print("\n %s" % dir(str));

	
