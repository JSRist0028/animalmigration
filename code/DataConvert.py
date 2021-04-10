# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:18:48 2021

@author: Justin Rist
"""

# Script used to convert MoveBank data into correct format for entry into neural net

import pandas
import csv

# import raw dataset from movebank (if you would like to do different dataset, change file reference) and create .csv for input into neural net

rawdata = pandas.read_csv("https://raw.githubusercontent.com/JSRist0028/animalmigration/main/data/Azores%20Great%20Whales%20Satellite%20Telemetry%20Program%20.csv")
sortdata = rawdata.sort_values(by = ['tag-local-identifier', 'timestamp'])

with open('C:/Users/Justin Rist/Desktop/WhaleData.csv', mode = 'w', newline = '') as netdata:
    netdata_writer = csv.writer(netdata, delimiter = ',')
    
    # headers for new csv
    
    netdata_writer.writerow(['AnimalID', 'TS', 'Lat', 'Long', 'TS - 1', 'Lat - 1', 'Long - 1'])
    
    # iterate through unique animals

    for animal in sortdata['tag-local-identifier'].unique():
        
        #iterate through timestamps of unique animal
        
        obscount = sortdata[sortdata['tag-local-identifier'] == animal].shape[0]
        obslist = sortdata.index[sortdata['tag-local-identifier'] == animal].tolist()
        
        for obs in range(1, obscount, 1):
            
            netdata_writer.writerow([animal, sortdata['timestamp'][obslist[obs]], sortdata['location-lat'][obslist[obs]], sortdata['location-long'][obslist[obs]],
                                    sortdata['timestamp'][obslist[obs - 1]], sortdata['location-lat'][obslist[obs - 1]], sortdata['location-long'][obslist[obs - 1]]])