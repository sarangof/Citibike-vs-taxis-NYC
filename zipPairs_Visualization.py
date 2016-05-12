# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:59:22 2016

@author: saf537
"""

import seaborn as sns
import matplotlib.pyplot as plt 
     
# This is a mockup of what would be **Jiheng's list**.
     
import itertools
import random
    
cbikelist = [10001, 10002, 10003, 10004, 10005, 10007, 10009, 10010, 10011, 10012, 10013, 10014, 10016, 10017, 10018, 10019, 10021, 10022, 10023, 10024, 10028, 10036, 10038, 10065, 10075, 10280, 10281, 10282, 11101, 11201, 11205, 11206, 11211, 11216, 11217, 11220, 11221, 11222, 11233, 11238, 11251]
dist_dict = {}
for subset in itertools.product(cbikelist,cbikelist):
    dist_dict[str(subset[0])+str(subset[1])] = random.randint(2,200)
    
    

"""
Create pairs for total trips
"""

f = open('./results/results_TotalJanMaySept', 'r')
pairs = f.read().split("\n")

dict_total = {}
zip_pair_pre = None
cnt = 0
tm_list = []
mode_list = []
for item in pairs[:-1]:
    print(item)
    trip, av_time, count = item.split("\t") #  
    zip_pair, mode = trip.split("|")
    zip_origin, zip_destin = zip_pair[:5], zip_pair[5:]
    if zip_pair == zip_pair_pre:
        cnt += 1
    else:
        if cnt == 2 and len(set(mode_list))==2:
            dict_total[zip_pair_pre] = [100*((float(tm_list[-2:][1]) - float(tm_list[-2:][0]) )/ float(tm_list[-2:][1])), dist_dict[zip_pair_pre] ]
            print("Si")
            tm_list = []
            mode_list = []
        cnt=1
    zip_pair_pre = zip_pair
    tm_list.append(av_time)
    mode_list.append(mode)

plt.vlines([val[1] for val in dict_total.values()], [0],[val[0] for val in dict_total.values()])

"""

Crete pairs for weekday rush vs. non-rush scenarios.

"""

f = open('./results/results_RushJanMaySept', 'r')
pairs = f.read().split("\n")

dict_rush = {}
zip_pair_pre = None
cnt = 0
tm_list = []
mode_list = []
for item in pairs[:-1]:
    print(item)
    trip, av_time, count = item.split("\t") #  
    zip_pair, form = trip.split("|")
    mode, rush = form.split("&")
    zip_origin, zip_destin = zip_pair[:5], zip_pair[5:]
    if zip_pair == zip_pair_pre:
        cnt += 1
    else:
        if cnt == 4 and len(set(mode_list))==2:
            # citibike&rush, citibike&valley, taxis&rush, taxis&valley 
            dict_rush[zip_pair_pre] = [['rush','valley'],  [100*((float(tm_list[-4:][2]) - float(tm_list[-4:][0]) )/ float(tm_list[-4:][2]) ),100*((float(tm_list[-4:][3]) - float(tm_list[-4:][1]) )/ float(tm_list[-4:][3]) ) ] , dist_dict[zip_pair_pre]] #100*((float(tm_list[-2:][1]) - float(tm_list[-2:][0]) )/ float(tm_list[-2:][1])) 
            print("Si")
            tm_list = []
            mode_list = []
        cnt=1
    zip_pair_pre = zip_pair
    tm_list.append(av_time)
    mode_list.append(mode)



"""

Crete pairs for weekend day vs-night scenarios.

"""
    
f = open('./results/results_SaturdayJanMaySept', 'r')
pairs = f.read().split("\n")

dict_weekend = {}
zip_pair_pre = None
cnt = 0
tm_list = []
mode_list = []
for item in pairs[:-1]:
    print(item)
    trip, av_time, count = item.split("\t") #  
    zip_pair, form = trip.split("|")
    mode, rush = form.split("&")
    zip_origin, zip_destin = zip_pair[:5], zip_pair[5:]
    if zip_pair == zip_pair_pre:
        cnt += 1
    else:
        if cnt == 4 and len(set(mode_list))==2:
            # citibike&rush, citibike&valley, taxis&rush, taxis&valley 
            dict_weekend[zip_pair_pre] = [['day','night'],  [100*((float(tm_list[-4:][2]) - float(tm_list[-4:][0]) )/ float(tm_list[-4:][2]) ),100*((float(tm_list[-4:][3]) - float(tm_list[-4:][1]) )/ float(tm_list[-4:][3]) ) ], dist_dict[zip_pair_pre] ] #100*((float(tm_list[-2:][1]) - float(tm_list[-2:][0]) )/ float(tm_list[-2:][1])) 
            print("Si")
            tm_list = []
            mode_list = []
        cnt=1
    zip_pair_pre = zip_pair
    tm_list.append(av_time)
    mode_list.append(mode)
    

# -- Save dictionaries in json files  
  
import json
with open('./results/total_trips.json', 'w') as fp:
    json.dump(dict_total, fp)
    
with open('./results/rush_nonrush.json', 'w') as fp:
    json.dump(dict_rush, fp)

with open('./results/total_weekends.json', 'w') as fp:
    json.dump(dict_weekend, fp)  
     