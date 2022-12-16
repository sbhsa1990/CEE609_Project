# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:12:46 2021

@author: Babak Asadollah
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import Dataset
data = pd.read_excel('305_Point_Future_Firemask.xlsx')
Date = data[['Date']]

# Cound number of 8 and 9 Fire mask labels in each day
MC_Fire_Mask = (data == 8).astype(int).sum(axis=1)
HC_Fire_Mask = (data == 9).astype(int).sum(axis=1)

# Construct a new dataset including count of 8 and 9 as well as Date
MC_Fire_Mask = pd.DataFrame(MC_Fire_Mask)
HC_Fire_Mask = pd.DataFrame(HC_Fire_Mask)
Date = pd.concat([Date, MC_Fire_Mask, HC_Fire_Mask], axis=1)
Date.columns = ['Date', 'MC', 'HC']

# Create annual monthly timeseries plot
mc_mean_annual = Date.groupby(Date['Date'].dt.year)['MC'].agg(['mean'])
hc_mean_annual = Date.groupby(Date['Date'].dt.year)['HC'].agg(['mean'])
mean_annual = pd.concat([mc_mean_annual, hc_mean_annual], axis=1)
mean_annual.columns = ['MC mean', 'HC mean']


mc_max_annual = Date.groupby(Date['Date'].dt.year)['MC'].agg(['max'])
hc_max_annual = Date.groupby(Date['Date'].dt.year)['HC'].agg(['max'])
maximum_annual = pd.concat([mc_max_annual, hc_max_annual], axis=1)
maximum_annual.columns = ['MC max', 'HC max']


mean_annual.plot.line(color=['orange', 'green'] , linewidth=3)
plt.xlabel("Year",  size = 15)
plt.ylabel("Average # of occurence", size = 15)
plt.title("Average occurence of future fire event", size = 15)
plt.xticks(range(2030, 2050, 2))
plt.savefig('Annual_mean.png', dpi = 300)

maximum_annual.plot.line(color=['blue', 'red'] , linewidth=3)
plt.xlabel("Year",  size = 15)
plt.ylabel("Maximum # of occurence", size = 15)
plt.title("Maximum occurence of future fire event", size = 15)
plt.xticks(range(2030, 2050, 2))
plt.savefig('Annual_max.png', dpi = 300)


# Create monthly timeseries plot
mc_mean_monthly = Date.groupby(Date['Date'].dt.month)['MC'].agg(['mean'])
hc_mean_monthly = Date.groupby(Date['Date'].dt.month)['HC'].agg(['mean'])
mean_monthly = pd.concat([mc_mean_monthly, hc_mean_monthly], axis=1)
mean_monthly.columns = ['MC mean monthly', 'HC mean monthly']

mc_max_monthly = Date.groupby(Date['Date'].dt.month)['MC'].agg(['max'])
hc_max_monthly = Date.groupby(Date['Date'].dt.month)['HC'].agg(['max'])
maximum_monthly = pd.concat([mc_max_monthly, hc_max_monthly], axis=1)
maximum_monthly.columns = ['MC max monthly', 'HC max monthly']

mean_monthly.plot.line(color=['orange', 'green'] , linewidth=3)
plt.xlabel("Month",  size = 15)
plt.ylabel("Average monthly occurence", size = 15)
plt.title("Average monthly occurence in future", size = 15)

plt.xticks(range(0, 12, 1))
plt.savefig('Monthly_mean.png', dpi = 300)

maximum_monthly.plot.line(color=['blue', 'red'] , linewidth=3)
plt.xlabel("Month",  size = 15)
plt.ylabel("Maximum monthly occurence", size = 15)
plt.title("Maximum monthly occurence in future", size = 15)
plt.xticks(range(0, 12, 1))
plt.savefig('Monthly_max.png', dpi = 300)