#!/usr/local/bin/python

import json
d = dict (name = 'Bob', age = 20, score = False);
j=json.dumps(d);

l=json.loads(j);

print(l['name']);
print(j);

