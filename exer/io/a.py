#!/usr/local/bin/python
import base64


with open("/usr/local/bin/python", "rb") as p:
	with open("a.txt", "w") as j:
		j.write( str(base64.b64encode(p.read())) );

exit(-1);

with open("/usr/local/bin/python", "rb") as s:
	print(s.read());

exit(-1);

with open("/etc/passwd", "r") as f :
	for line in f.readlines():
		print(line.strip())

exit(-1);

try:
	f = open("/etc/passwd", "r");
	print(f.read());
	print("%d", 1/0);
except BaseException as e:
	print("exception:", e);
finally:
	f.close();
