# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 17:18:48 2021

@author: Justin Rist
"""

# Script used to convert MoveBank data into correct format for entry into neural net

import pandas
import csv

# import raw dataset from movebank (if you would like to do different dataset, change file reference) and create .csv for input into neural net

    # Whale data link: "https://raw.githubusercontent.com/JSRist0028/animalmigration/main/data/Azores%20Great%20Whales%20Satellite%20Telemetry%20Program%20.csv"
    # Goose data link: "https://raw.githubusercontent.com/JSRist0028/animalmigration/main/data/barnacle_geese_data_matrix.csv"
    
    # 'tag-local-identifier', 'location-lat', 'location-long' for whale
    # 'birdID', 'latitude', 'longitude' for goose
        
animalID = 'birdID'
latID = 'latitude'
longID = 'longitude'


rawdata = pandas.read_csv("https://raw.githubusercontent.com/JSRist0028/animalmigration/main/data/barnacle_geese_data_matrix.csv")
sortdata = rawdata.sort_values(by = [animalID, 'timestamp'])

    # change created file name/path here

with open('C:/Users/Justin Rist/Desktop/GooseData.csv', mode = 'w', newline = '') as netdata:
    netdata_writer = csv.writer(netdata, delimiter = ',')
    
    # headers for new csv
    
    netdata_writer.writerow(['AnimalID', 'TS', 'Lat', 'Long', 'TS - 1', 'Lat - 1', 'Long - 1'])
    
    # iterate through unique animals

    for animal in sortdata[animalID].unique():
        
        # iterate through timestamps of unique animal
        
        obscount = sortdata[sortdata[animalID] == animal].shape[0]
        obslist = sortdata.index[sortdata[ animalID] == animal].tolist()
        
        for obs in range(1, obscount, 1):
            
            netdata_writer.writerow([animal, sortdata['timestamp'][obslist[obs]], sortdata[latID][obslist[obs]], sortdata[longID][obslist[obs]],
                                    sortdata['timestamp'][obslist[obs - 1]], sortdata[latID][obslist[obs - 1]], sortdata[longID][obslist[obs - 1]]])