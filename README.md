# CEE609_Project

Forest fire is considered as an environmental hazard which frequently threats the various regions across the world. The frequent occurrence of fire incidents in forested areas at northern Iran forced significant socioeconomic casualties. This study aims to develop a forecasting tool in order to determine the significance of forest fire levels in the Hyrcanian forest, Golestan, Iran. 

MODIS MOD14A2 fire products between 2000 to 2021 has been regarded as the target of classification. Products of MOD14A2, which consists of fire-mask and quality affirmation algorithm, has the spatial and temporal resolution of 1-kilometer and 8 days and provides gridded level-3 data in the Sinusoidal projection. The data has been downloaded from "APPEEARS" platform [https://appeears.earthdatacloud.nasa.gov/]. Using this link, in section of "area samples" you must upload the "Golestan_Shapefile.zip" as the selected region. For date you must select the 2000 to 2021, and for section of "layers to include in the sample" the "Terra MODIS Thermal Anomalies and Fire, MOD14A3.006, 1000m, 8day" must be selected. The NetCDF-4 has also been selected as the output extension [MODIS_Golestan.nc].


Using "Extract_From_MODIS.py", the geographical location (Latitude and Longitude) of points with three fire mask (no fire (labeled as 5), medium fire confidence (labeled as 8) and high fire confidence (labeled as 9)) has been extracted. The "Files_location.xlsx" file is the output of this process which clarifies the Point, their Latitude and Longitude and Fire_mask lable.

Using "Files_location.xlsx", the observed varibles from "Famine Early Warning Systems Network (FEWS NET) Land Data Assimilation System (FLDAS)" have been extracted.
The employed “FLDAS_NOAH001_G_CA_D” includes 18 variables modeled from the NOAH 3.6.1 and Land Information System (LIS7). One of the major advantage of this satellite, which makes it more suitable for the subject of this study, is its particular concentration on Central Asia region with specific spatial coverage of 21.0°~30.0°E and 56.0°~100.0°N. FLDAS also benefits from very fine spatial resolution of 0.01° and daily temporal resolution which stretches from 2000-10-01 to the present day [https://disc.gsfc.nasa.gov/datasets/FLDAS_NOAH001_G_CA_D_001/summary]. 

   Variables name            Description:  
1 'Swnet_tavg'                surface_net_downward_shortwave_flux 

2 'Rainf_tavg'                precipitation_rate

3 'Evap_tavg'                 total_evapotranspiration 

4 'Qs_tavg'                   surface_runoff_amount  

5 'RadT_tavg'                 surface_radiative_temperature  

6 'Rainf_f_tavg'              rainfall_flux

7 'Tair_f_tavg'               air_temperature 

8 'Qair_f_tavg'               specific_humidity 

9 'Psurf_f_tavg'              surface_air_pressure 

10 'SWdown_f_tavg'            surface_downwelling_shortwave_flux_in_air

11 'SoilMoi00_10cm_tavg'      soil moisture content @ 10cm

12 'SoilMoi10_40cm_tavg'      soil moisture content @ 40cm

13 'SoilMoi40_100cm_tavg'     soil moisture content @ 100cm

14 'SoilMoi100_200cm_tavg'    soil moisture content @ 200cm

15 'SoilTemp00_10cm_tavg'     soil_temperature @ 10cm

16 'SoilTemp10_40cm_tavg'     soil temperature @ 40cm

17 'SoilTemp40_100cm_tavg'    soil temperature @ 100cm

18 'SoilTemp100_200cm_tavg'   soil temperature @ 200cm
 
Using the "Files_location.xlsx" as the output of "Extract_From_MODIS.py" and also by utilizing the "Extract_FLDAS.py" code,  values of 18 variables at each points is extracted and aggregated as the Final dataset to be used as regression model input.

