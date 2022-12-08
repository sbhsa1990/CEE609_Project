# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 15:41:18 2022

@author: Riley
"""

import numpy as np
import pandas as pd  
import math
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from statistics import mean
from sklearn.preprocessing import MinMaxScaler
import glob


fileList=glob.glob("*.xlsx")
for filename in fileList:
    data = pd.read_excel(filename)
    X = data.drop(['Target'],1)
    x = pd.DataFrame(X)
    Y = data['Target']
    y = pd.DataFrame(Y)
    
    e = pd.DataFrame()
    for column in x:
        column_01 = y
        column_02 = x[column].values
        column_02 = pd.DataFrame(column_02)
        concatDF = pd.concat((column_01,column_02),axis=1)
        concatDF.columns=['y_test', 'yhat']
        column_1 = concatDF["y_test"]
        column_2 = concatDF["yhat"]
        A = column_1.corr(column_2)
        R = abs(A)
        
        # RMSE
        MSE = mean_squared_error(column_1, column_2)
        RMSE = math.sqrt(MSE)
        
        # MAE
        MAE = mean_absolute_error(column_1, column_2)
        
        # NSE
        average = mean(column_1)
        diff = column_1 - column_2
        diff2 = Y - average
        sqr_1 = diff**2
        sqr_2 = diff2**2
        sumsqr_1=sqr_1.sum()
        sumsqr_2=sqr_2.sum()
        NSE = (1-(sumsqr_1/sumsqr_2))

        e = e.append(pd.DataFrame({'CC':[R], 'RMSE':[RMSE], 'MAE':[MAE], 'NSE':[NSE]}))
        
    # Normalize the metric dataframe
    scaler = MinMaxScaler()
    scaled_metric_df = scaler.fit_transform(e)
    scaled_metric_df = pd.DataFrame(scaled_metric_df)
    
    # Calcualte the average of each row
    average_col = scaled_metric_df.mean(axis=1)
    average_col = pd.DataFrame(average_col)
    scaled_metric_df.insert(0, 'Mean', average_col)
    
    
    Final_0 = pd.DataFrame(x.columns)
    
    dff = pd.concat([Final_0, scaled_metric_df], axis=1, ignore_index=False)
    dff.columns = ['CMIP6 source', 'Mean', 'R', 'RMSE', 'MAE', 'NSE']
    
    # saving the excel
    file_name = 'Normalized_Metrics-' + filename
    dff.to_excel(file_name)
    