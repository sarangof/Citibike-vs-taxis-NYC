# -*- coding: utf-8 -*-
"""
Created on Wed May 11 11:16:55 2016

@author: saf537
"""

import json
json_data1=open('./data/stationzips.json').read()
zipStations = json.loads(json_data1)
uniqueZip_Stations = sorted(list(set(zipStations.values())))[2:]

f=open('./data/uniqueCitiBikeZips.txt','w')
for ele in uniqueZip_Stations:
    f.write(str(ele)+'\n')

f.close()