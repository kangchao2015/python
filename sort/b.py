#/usr/local/bin/python

def count():
    fs = []
    for i in range(1, 4):
        def f():
             def j():
                   return i*i
             return j;
        fs.append(f())
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3());
