# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:22:00 2021

@author: Justin Rist
"""

# Script used to split data into training and testing set

import pandas
import math

# Function for splitting the data into testing and training sets

def train_test_split(datafile, train_ratio):
    
    # Define dataframes to return
    
    headers = ['AnimalID', 'TS', 'Lat', 'Long', 'TS - 1', 'Lat - 1', 'Long - 1']
    train = pandas.DataFrame(columns = headers)
    test = pandas.DataFrame(columns = headers)
    
    # Split each unique animal tracking info into training and testing sets
    
    for animal in datafile['AnimalID'].unique():
        traincount = math.ceil(float(datafile[datafile['AnimalID'] == animal].shape[0]) * train_ratio)
        obscount = datafile[datafile['AnimalID'] == animal].shape[0]
        obslist = datafile.index[datafile['AnimalID'] == animal].tolist()
        
        for obs in range(0, traincount, 1):
            df = [animal, datafile['TS - 1'][obslist[obs]], datafile['Lat'][obslist[obs]], datafile['Long'][obslist[obs]],
                                  datafile['TS - 1'][obslist[obs]], datafile['Lat - 1'][obslist[obs]], datafile['Long - 1'][obslist[obs]]]
            
            train.loc[len(train.index)] = df
    
        for obs in range(traincount, obscount, 1):
            df = [animal, datafile['TS - 1'][obslist[obs]], datafile['Lat'][obslist[obs]], datafile['Long'][obslist[obs]],
                                  datafile['TS - 1'][obslist[obs]], datafile['Lat - 1'][obslist[obs]], datafile['Long - 1'][obslist[obs]]]
            
            test.loc[len(test.index)] = df
    
    return(train, test)
