#!/usr/local/bin/python

import base64

with open("a.txt", "r") as f:
	with open("b.out", "wb") as w:
		w.write(str(base64.b64decode(f.read())));
