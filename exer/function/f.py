#!/usr/local/bin/python


nums = [1,2,3,4,5]
def aa(*nums):
	a = 0;
	for i in nums:
		a = a + i * i;
	return a;

print(aa(*nums));


ll = {'asdf':'asdfasdf','z':'asdfsadf'}

def bb(name, age, **kw):
	print("name %s age: %d" % (name, age));
	print(kw);


def cc(a, b,c=0, *d, e,f, **g):
print("a:", a, "b:", b, "c:", c, "d:", d, "e f ", e,f , "g", g)

#bb("asdf", 12, city="kkk", pos='asdf');
#bb('123',99, **ll)



cc(1,2,3,3,4,5, e='asfd', f='zzzz', g='sadfsdfadsf',h= 'asdfasdf');
