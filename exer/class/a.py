#/usr/local/bin/python


class a():

	def __init__(self, name, socre):
		self.__name = name;
		self.socre = socre;

	def show(self):
		print("name:", self.__name, "score:", self.socre);

	def set_name(self, name):
		self.__name = name;
	
	def get_name(self):
		return self.__name;
		

p = a("asdfasdf", 99);
p.__name = "kangchao"
print("%s" % p.get_name());
print("%s" % p.__name);

p.show();

