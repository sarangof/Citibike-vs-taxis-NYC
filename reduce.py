#!/usr/bin/python

import sys
import datetime

current_duration = 0.
current_key = None
current_count = 0

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
#	print line

	key, duration = line.strip().split("\t")
	try:
		duration = int(duration)
	except ValueError:
		continue

	if key == current_key:
		current_count += 1
		current_duration += duration
	else:
		if current_key:
			print "%s\t%d \t %s" % (key, float(current_duration)/float(current_count), current_count)
		current_duration = duration
		current_key = key
		current_count = 1

