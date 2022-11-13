

from netCDF4 import Dataset
import numpy as np
import pandas as pd

data = Dataset('MODIS_Golestan.nc', 'r')

# Find the variable characteristics
lon = data.variables['lon'][:]
lat = data.variables['lat'][:]
t = data.variables['time'][:]

# Extract the output based on (time, latitude, longitude)
# 496 is the time of event

fire = data.variables['FireMask'][496,:,:]      

# Find pecific values (e.g. 7,8 and 9's) row/column index in the array
c = np.where(fire==9)
cn = list(zip(c[0],c[1]))
cndf = pd.DataFrame(cn)
cndf['Fire'] = '9'


b = np.where(fire==8)
bn = list(zip(b[0],b[1]))
bndf = pd.DataFrame(bn)
bndf = bndf.sample(n = 50)
bndf['Fire'] = '8'

d = np.where(fire==5)
dn = list(zip(d[0],d[1]))
dndf = pd.DataFrame(dn)
dndf = dndf.sample(n = len(cn))
dndf['Fire'] = '5'


# Build a dataframe containing lat and lon of the specific values
coordinates = bndf.append(cndf).append(dndf)
coordinates.columns =['lat', 'lon', 'Fire']


# Build a dataframe from "lat" array
lat_df = pd.DataFrame(lat)
lat_df = lat_df.rename(columns = {0:"degree"})

# Add a new column to dataframe with the label of "index" ...
# ... containing 0 to n (length of lat array)
lat_df['index'] = np.arange(len(lat_df))

# Same procedure with "lon" array
lon_df = pd.DataFrame(lon)
lon_df = lon_df.rename(columns = {0:"degree"})
lon_df['index'] = np.arange(len(lon_df))


# Repalce the index values of lat and lon with corresponding degree value
coordinates2 = (coordinates[coordinates['lat'].isin(lat_df['index'])]
                .assign(latitude=lambda x: x['lat'].map(lat_df.set_index('index')['degree'])))

coordinates3 = (coordinates[coordinates['lon'].isin(lon_df['index'])]
                .assign(longitude=lambda x: x['lon'].map(lon_df.set_index('index')['degree'])))

Final = pd.concat([coordinates2, coordinates3], axis=1)

# Delete unnecessary columns
Final = Final.drop(['lat', 'lon'], axis=1)
Final = Final.iloc[: , 1:]

# Sort the columns
Final = Final[['latitude', 'longitude', 'Fire']]

Final.reset_index(drop=True, inplace=True)
Final = Final.sort_values(by=['latitude'])
Final.reset_index(drop=True, inplace=True)


x = pd.DataFrame()
x['numbers'] = np.arange(start=1, stop=len(Final)+1, step=1, dtype=int)
x['p'] = 'P'
x["Points"] = x["p"] + x["numbers"].astype(str)
Points = x.drop(['p', 'numbers'], axis=1)

Final = pd.concat([Final, Points], axis=1)

file_name = 'Files_location.xlsx' 
Final.to_excel(file_name)

