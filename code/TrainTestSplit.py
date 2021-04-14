# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 11:22:00 2021

@author: Justin Rist
"""

# Script used to split data into training and testing set

import pandas
import math

# Function for splitting the data into testing and training sets

def train_test_split(datafile, tomorrow, train_ratio, includetemp):
    
    # Define dataframes to return
    
    xheaders = ['AnimalID', 'TS', 'Lat - 1', 'Long - 1']
    yheaders = ['AnimalID', 'Lat', 'Long']
    
    trainx = pandas.DataFrame(columns = xheaders)
    trainy = pandas.DataFrame(columns = yheaders)
    testx = pandas.DataFrame(columns = xheaders)
    testy = pandas.DataFrame(columns = yheaders)
    
    # Split each unique animal tracking info into training and testing sets
    
    for animal in datafile[0].unique():
        traincount = math.ceil(float(datafile[datafile[0] == animal].shape[0]) * train_ratio)
        obscount = datafile[datafile[0] == animal].shape[0]
        obslist = datafile.index[datafile[0] == animal].tolist()
        
        for obs in range(0, traincount, 1):
            dfx = [animal, datafile[1][obslist[obs]], datafile[2][obslist[obs]], datafile[3][obslist[obs]]]
            dfy = [animal, tomorrow[1][obslist[obs]], tomorrow[2][obslist[obs]]]
            
            trainx.loc[len(trainx.index)] = dfx
            trainy.loc[len(trainy.index)] = dfy
    
        for obs in range(traincount, obscount, 1):
            dfx = [animal, datafile[1][obslist[obs]], datafile[2][obslist[obs]], datafile[3][obslist[obs]]]
            dfy = [animal, tomorrow[1][obslist[obs]], tomorrow[2][obslist[obs]]]
            
            testx.loc[len(testx.index)] = dfx
            testy.loc[len(testy.index)] = dfy
    
    return(trainx, trainy, testx, testy)
