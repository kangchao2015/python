#!/usr/local/bin/python

import base64

with open("a.out", "rb") as f:
	with open("b.txt", "w") as w:
		w.write(str(base64.b64encode(f.read())));
