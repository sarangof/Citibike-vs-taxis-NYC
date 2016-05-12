#!/usr/bin/python

import sys
import datetime
import geopandas as gp

zipcodes = gp.read_file('NYCzipcodeshapefile2.geojson') # ??? How should we import this best?
g=open('uniqueCitiBikeZips.txt')
#uniqueCBikeZips = g.read().split('\t')
#uniqueCBikeZips = uniqueCBikeZips[:-1]
#uniqueCBikeZips = map(int, uniqueCBikeZips)

uniqueCBikeZips = [10001, 10002, 10003, 10004, 10005, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10021, 10022, 10023, 10024, 10028, 10036, 10038, 10065, 10075, 10280, 10281, 10282, 11101, 11201, 11205, 11206, 11211, 11216, 11217, 11220, 11221, 11222, 11233, 11238, 11251]

uniqueCBikeZips = map(int, uniqueCBikeZips)

for line in sys.stdin:
	l = line.strip().split(',') #header condition

	if ((len(l) == 19) & (l[0] != 'VendorID')):

	        pt_origin = gp.geoseries.Point(float(l[5]),float(l[6])) # column order
        	pt_destin = gp.geoseries.Point(float(l[9]),float(l[10]))
        	pickup_time = datetime.datetime.strptime(l[1],"%Y-%m-%d %H:%M:%S")
	        dropoff_time = datetime.datetime.strptime(l[2],"%Y-%m-%d %H:%M:%S")

		try:
			c = dropoff_time - pickup_time
			trip_duration = c.total_seconds()#divmod(c.days*86400 + c.seconds,60)
		except ValueError:
			continue

	        for x, z in enumerate(zipcodes['geometry']):
			if pt_origin.intersects(z):
				zip_origin = zipcodes['postalCode'][x]
				break
		for x, z in enumerate(zipcodes['geometry']):
        	        if pt_destin.intersects(z):
				zip_destin = zipcodes['postalCode'][x]
				break
                try:
                        trip_duration = int(trip_duration)
			#print int(zip_origin)
			#print int(zip_destin)
			if int(zip_origin) in uniqueCBikeZips and int(zip_destin) in uniqueCBikeZips:
				print "%s\t%s"% (str(zip_origin)+str(zip_destin)+"|"+"taxis",trip_duration) #Very careful, formatting.
		except ValueError:
			continue		


        #Citibike
        elif ((len(l) == 15) & (l[0] != 'tripduration')):
		if l[12] == 'Subscriber':
			pt_origin = gp.geoseries.Point(float(l[6]),float(l[5]))
		
			# Origin   
			for x, z in enumerate(zipcodes['geometry']):
				if pt_origin.intersects(z):
					zip_origin = zipcodes['postalCode'][x]
					break
			# Destination:
			pt_destin = gp.geoseries.Point(float(l[10]),float(l[9]))
			for x, z in enumerate(zipcodes['geometry']):
				if pt_destin.intersects(z):
					zip_destin = zipcodes['postalCode'][x]
					break

			try:
				l[0] = int(l[0])
				print "%s\t%s"% (str(zip_origin)+str(zip_destin)+"|"+"citibike",l[0]) #Very careful, formatting.

                	except ValueError:
				continue

