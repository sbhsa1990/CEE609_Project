# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 16:20:23 2021

@author: Babak Asadollah
"""


from netCDF4 import Dataset 
import pandas as pd
import numpy as np
import glob
import math
    

# Get the variables data from one sample FLDAS NC4 file
data = Dataset('FLDAS_NOAH001_G_CA_D.A20160711.001.nc.SUB.nc4', 'r')
lat = data.variables['lat'][:]
lon = data.variables['lon'][:]
t = data.variables['time'][:]

'''
# Variables name and description:
    
 'Swnet_tavg'       surface_net_downward_shortwave_flux 
 'Rainf_tavg'       precipitation_rate
 'Evap_tavg'        total_evapotranspiration 
 'Qs_tavg'          surface_runoff_amount   
 'RadT_tavg'        surface_radiative_temperature    
 'Rainf_f_tavg'     rainfall_flux
 'Tair_f_tavg'      air_temperature  
 'Qair_f_tavg'      specific_humidity   
 'Psurf_f_tavg'     surface_air_pressure  
 'SWdown_f_tavg'    surface_downwelling_shortwave_flux_in_air
 
 'SoilMoi00_10cm_tavg'      soil moisture content @ 10cm
 'SoilMoi10_40cm_tavg'      soil moisture content @ 40cm
 'SoilMoi40_100cm_tavg'     soil moisture content @ 100cm
 'SoilMoi100_200cm_tavg'    soil moisture content @ 200cm
  
 'SoilTemp00_10cm_tavg'     soil_temperature @ 10cm
 'SoilTemp10_40cm_tavg'     soil temperature @ 40cm
 'SoilTemp40_100cm_tavg'    soil temperature @ 100cm
 'SoilTemp100_200cm_tavg'   soil temperature @ 200cm
'''

var = data.variables
var = list(var)
var_df = pd.DataFrame(var, columns =['vari']) 
var_df = var_df[4:]
var_df.reset_index(drop=True, inplace=True)

e = pd.DataFrame()
g = pd.DataFrame()

cities = pd.read_excel('Files_location.xlsx')

for index, row in cities.iterrows():
    location = row['Points']
    location_latitude = row['lat']
    location_longitude = row['lon']
    
    fileList=glob.glob("*.nc4")
    for filename in fileList:
        data = Dataset(filename, 'r')
        lon = data.variables['lon'][:]
        lat = data.variables['lat'][:]
        t = data.variables['time'][:]
    
        for i, row in var_df.iterrows():
            variable = row['vari']
            f = pd.DataFrame()
 
            sq_diff_lat = (lat - location_latitude)**2 
            sq_diff_lon = (lon - location_longitude)**2    
            min_index_lat = sq_diff_lat.argmin()
            min_index_lon = sq_diff_lon.argmin()
                
            Z1 = data.variables[variable][:, min_index_lat, min_index_lon] 
        
            f = e.append(pd.DataFrame(Z1))
            f.reset_index(drop=True, inplace=True)
                
file_name = location + variable + '.xlsx' 
 # saving the excel
f.to_excel(file_name)



