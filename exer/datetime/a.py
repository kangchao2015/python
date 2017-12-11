#!/usr/local/bin/python


from datetime import datetime, timedelta, timezone


now = datetime.now();
now1 = datetime(1,2,3,4,5,6);
t1 = now1.timestamp();
cday = datetime.strptime('1999-09-01 12:12:12', '%Y-%m-%d %H:%M:%S');

print(now);
print(now.timestamp());
print(now1.timestamp());
print(datetime.fromtimestamp(t1));
print(cday.timestamp());

cday1 = cday + timedelta(days = 1)
print(cday1);
