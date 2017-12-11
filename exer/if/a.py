#!/usr/local/bin/python

h = input("please input your height(cm)");
w = input("please input your weight(kg)");

h = int(h);
w = int(w);

bmi = w / h / h * 10000;

print(bmi);

if bmi < 18.5 :
	print("light");
elif bmi < 25 :
	print("normal");
elif bmi <32 :
	print("over weight");
else :
	print("too fat");

