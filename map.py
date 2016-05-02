#!/usr/bin/python

import sys
import datetime
import geopandas as gp

zipcodes = gp.read_file('NYCzipcodeshapefile2.geojson') # ??? How should we import this best?

for line in sys.stdin:
	l = line.strip().split(',') #header condition
	if len(l) == 19: #Figure this out
		# taxis
		pt_origin = gp.geoseries.Point(l.lon_origin,l.lat_origin) # column order
		for x,z in enumerate(zipcodes['geometry']):
    			if pt.intersects(z):
        			zip_origin = zipcodes['postalCode']
				break
		pt_destin = gp.geoseries.Point(l.lon_destin,l.lat_destin) # column order
		for x,z in enumerate(zipcodes['geometry']):
    			if pt.intersects(z):
        			zip_destin = zipcodes['postalCode']
				break
		try l.start_time - l.end_time: #Good condition here # column order
			print "%s\t%d"% (str(zip_origin)+str(zip_destin),l.start_time - l.end_time) #Very careful, formatting. # column order
	elif len(l)==15: #Figure this out
		#bicycles
		try l.start_time - l.end_time: #Good condition here
			print "%s\t%d"% (str(zip_origin)+str(zip_destin),l.start_time - l.end_time) #Very careful, formatting.

"""

# They have to come somewhere in the input or...somewhere?
zip_origin = 11201
zip_destination = 10002 # input comes from STDIN (stream data that goes to the program)

if zip_taxis_origin == zip_origin and zip_taxis_destination == zip_destination:

"""
