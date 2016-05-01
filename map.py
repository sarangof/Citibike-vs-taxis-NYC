#!/usr/bin/python

import sys
import datetime
import geopandas as gp

# They have to come somewhere in the input or...somewhere?
zip_origin = 11201
zip_destination = 10002 # input comes from STDIN (stream data that goes to the program)

for line in sys.stdin:
	l = line.strip().split(',') #header condition
	if len(l) == 5: #Figure this out
		# taxis
		if zip_taxis_origin == zip_origin and zip_taxis_destination == zip_destination:
			if l.start_time - l.end_time: #Good condition here
				print "%s\t%d"% (str(zip_origin)+str(zip_destination),l.start_time - l.end_time) #Very careful, formatting.
	elif len(l)==7: #Figure this out
		#bicycles
		if zip_taxis_origin == zip_origin and zip_taxis_destination == zip_destination:
			if l.start_time - l.end_time: #Good condition here
				print "%s\t%d"% (str(zip_origin)+str(zip_destination),l.start_time - l.end_time) #Very careful, formatting.
