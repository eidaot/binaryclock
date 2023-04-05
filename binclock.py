#!/usb/bin/python

from time import localtime
import os, time

#change to a 1 for military time (24 hour format)
use_military=1

def int2bin(n, count=6):
    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

while 1:
	os.system("clear")
	ampm=localtime()[3]
	if not use_military:
		if ampm > 12:
			ampm = ampm - 12
	print int2bin(ampm)
	print int2bin(localtime()[4])
	print int2bin(localtime()[5])
	time.sleep(1)

