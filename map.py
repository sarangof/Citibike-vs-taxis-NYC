#!/usr/bin/python

import sys
import datetime
import geopandas as gp

zipcodes = gp.read_file('/user/saf537/FinalProject/NYCzipcodeshapefile2.geojson') # ??? How should we import this best?

for line in sys.stdin:
	l = line.strip().split(',') #header condition
	pt_origin = gp.geoseries.Point(float(l[10]),float(l[11])) # column order
	print "%s \t %d" % (pt_origin,1)
#	pickup_time = datetime.datetime.strptime(l[1],"%Y-%m-%d %H:%M:%S")
#	dropoff_time = datetime.datetime.strptime(l[2],"%Y-%m-%d %H:%M:%S")
#	c = dropoff_time-pickup_time
#	trip_duration = divmod(c.days* 86400 + c.seconds,60)
#	for x,z in enumerate(zipcodes['geometry']):
#		if pt.intersects(z):
#			zip_origin = zipcodes['postalCode']
#			break

#	if len(l) == 19: #Figure this out
#		# taxis
		# pickup_time = 1, dropoff_time = 2, dropoff_longitude = 10, dropoff_latitude = 11, pickup_longitude = 5, pickup_latitude = 64
#		pt_origin = gp.geoseries.Point(float(l[5],float(l[6])) # column order
#		pickup_time = datetime.datetime.strptime(l[1],"%Y-%m-%d %H:%M:%S")
#		dropoff_time = datetime.datetime.strptime(l[2],"%Y-%m-%d %H:%M:%S")
#		c = dropoff_time-pickup_time
#		trip_duration = divmod(c.days* 86400 + c.seconds,60)

#		for x,z in enumerate(zipcodes['geometry']):
#    			if pt_origin.intersects(z):
#        			zip_origin = zipcodes['postalCode']1
#				break
#		pt_destin = gp.geoseries.Point(l[9].l[10]) # column order
#		for x,z in enumerate(zipcodes['geometry']):
#    			if pt_destin.intersects(z):
#        			zip_destin = zipcodes['postalCode']
#				break
#		try l.start_time - l.end_time: #Good condition here # column order
#			print "%s\t%d"% (str(zip_origin)+str(zip_destin),l.start_time - l.end_time) #Very careful, formatting. # column order
#	elif len(l)==15: #Figure this out
#		#bicycles
#		try l.start_time - l.end_time: #Good condition here
#			print "%s\t%d"% (str(zip_origin)+str(zip_destin),l.start_time - l.end_time) #Very careful, formatting.


