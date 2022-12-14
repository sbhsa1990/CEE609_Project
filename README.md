# CEE609 Project
Forest fire is considered as an environmental hazard which frequently threats the various regions across the world. The frequent occurrence of fire incidents in forested areas at northern Iran forced significant socioeconomic casualties. This study aims to develop a forecasting tool in order to determine the significance of forest fire levels in the Hyrcanian forest, Golestan, Iran. 

# Extarct data from satellite sources to structure the initial dataset
MODIS MOD14A2 fire products between 2000 to 2021 has been regarded as the target of classification. Products of MOD14A2, which consists of fire-mask and quality affirmation algorithm, has the spatial and temporal resolution of 1-kilometer and 8 days and provides gridded level-3 data in the Sinusoidal projection. The data has been downloaded from "APPEEARS" platform [https://appeears.earthdatacloud.nasa.gov/]. Using this link, in section of "area samples" you must upload the "Golestan_Shapefile.zip" as the selected region. For date you must select the 2000 to 2021, and for section of "layers to include in the sample" the "Terra MODIS Thermal Anomalies and Fire, MOD14A3.006, 1000m, 8day" must be selected. The NetCDF-4 has also been selected as the output extension [MODIS_Golestan.nc].

Using "Extract_From_MODIS.py", the geographical location (Latitude and Longitude) of points with three fire mask (no fire (labeled as 5), medium fire confidence (labeled as 8) and high fire confidence (labeled as 9)) has been extracted. The "Files_location.xlsx" file is the output of this process which clarifies the Point, their Latitude and Longitude and Fire_mask lable.

Using "Files_location.xlsx", the observed varibles from "Famine Early Warning Systems Network (FEWS NET) Land Data Assimilation System (FLDAS)" have been extracted.
The employed “FLDAS_NOAH001_G_CA_D” includes 18 variables modeled from the NOAH 3.6.1 and Land Information System (LIS7). One of the major advantage of this satellite, which makes it more suitable for the subject of this study, is its particular concentration on Central Asia region with specific spatial coverage of 21.0°~30.0°E and 56.0°~100.0°N. FLDAS also benefits from very fine spatial resolution of 0.01° and daily temporal resolution which stretches from 2000-10-01 to the present day [[https://disc.gsfc.nasa.gov/datasets/FLDAS_NOAH001_G_CA_D_001/summary](https://hydro1.gesdisc.eosdis.nasa.gov/data/FLDAS/FLDAS_NOAH001_G_CA_D.001/)]. 

The utilized variables include Surface net downward shortwave flux, precipitation rate, total evapotranspiration, surface runoff, surface radiative temperature,   rainfall flux, air temperature, specific humidity, surface air pressure, surface downwelling shortwave flux in air, soil moisture content @ 10cm, 40cm, 100cm and 200 cm, Soil_temperature @ 10cm, 40cm, 100cm and 200 cm.

Using the "Files_location.xlsx" as the output of "Extract_From_MODIS.py" and also by utilizing the "Extract_FLDAS.py" code,  values of 18 variables at each points is extracted and aggregated as the Final dataset to be used as classification model input. However, pre processing this initial dataset as well as considreing the multicollinearity between the variables leads to the optimal dataset containing only 10 most correlated variales which can be seen in "Inputs_dataset.xlsx" file in the repository.

# Train the classification algorithm
This dataset ("Inputs_dataset.xlsx") is then used as the input of "Gradient_Boosting_classification.py" as the classification algorithm. The Gradient Boosting classification has been employed form the "Scikit-Learn" and the parameters have been optimized so that the best results could be achieved. Next, Using the "Combination_Analysis.py" pythone code the most optimal combination of our initial 10 input has been extracted based on Precision, Recall, Balanced accuracy and F1 score classification accuracy metrics.

In order to compare the results of GBC, two other widely used machine learning algorithms known as Random Forest and Extra Tree classifiers are employed for comparison purposes only. To apply these three ensemble algorithms, the Scikit-Learn (SKlearn) machine learning library of Python programming language has been employed. The ensemble sub-category of SKlearn provides various regression and classification algorithm which operates based on tuning of several parameters.

sklearn.ensemble.GradientBoostingClassifier : 
[https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier]

sklearn.ensemble.RandomForestClassifier : 
[https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier]

sklearn.ensemble.ExtraTreesClassifier : 
[https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html#sklearn.ensemble.ExtraTreesClassifier]



# Produce figures to find correlation between FLDAS and CMIP6
The optimal model proved to has combination of [Qair, SoilMoi, Swnet, Tair] which respectively are specific humidity, soil moisture content @ 10cm, surface downwelling shortwave flux in air and air temperature.
In next stage, the projected NC files for each of these four parameters have been downloaded from CMIP6 platform using (https://esgdata.gfdl.noaa.gov/search/cmip6-gfdl/). These projections are mainly from 2020 to 2100, however, we are only interested in 2030 to 2060 as near future horizon.

The correspondong CMIP6 variables to [Qair, SoilMoi, Swnet, Tair] are respectively HUS, MRSO, RSDS and TAS. for each of these varibale the (Shared Socioeconomic Pathways) SSPs-1, -2 and -3 have been cosidered which somehow denote the good, mild and bat future scenarios. The output of CMIP6 are listed in "CMIP6 Dataset" folder in main repository. Next, we need to find out which CMIP6 SSPs are in better correlation with FLDAS's [Qair, SoilMoi, Swnet, Tair]. This task is carried out by utilizong the Scatter-plot visualization metric which represented as "Scatter_plot.py". Bellow are just some sample of generated Scatter-plots:

![Untitled-111](https://user-images.githubusercontent.com/114182572/206521305-c1b51868-8b50-4594-8fb4-27a740c6ad26.jpg)


Heatmap has been employed As another graphical evaluator. In order to obtain this plot we first need to find the accuracy metrics such as R (Correlation Coefficitn), RMSE (Root Mean Squared Error), MAE (Mean Absolute Erro) and NSE (Nash Sutcliffe Efficiency) between FLDAS's [Qair, SoilMoi, Swnet, Tair] and 15 CMIP6 obtained variables (5 GCM's and 3 SSP's). This task has been carried out using "Heatmap_Inputs.py" in "CMIP6 Dataset" folder of main repository. Outputs of this algorithm are saved in another folder in repository named "Heatmap". Utilizing the "Heatmap.py" script in that folder will eventually leads to 4 Heatmap plots named after [HUS, RSDS, MRSO and TAS]. In these plots the GCM-SSP model which has Black cells or normalized values closer to 1.00 is considered to be and overall good representor of FLDAS's [Qair, SoilMoi, Swnet, Tair].

![Heatmaps - Copy - Copy](https://user-images.githubusercontent.com/114182572/206520475-96d82f14-b23a-4009-be18-3a2dbf5a3650.jpg)

# Future projections
Based on our figures the following GCM's as well as SSP's are best simulators of FLDAS's [Qair, SoilMoi, Swnet, Tair]:
Qair:    HUSS-MIROC06-SSP245
SoilMoi: MRSO-MIROC06-SSP370
Swnet:   RSDS-MIROC06-SSP370
Tair:    TAS -MIROC06-SSP370

For future projections we only consider 305 point in Historical period with High Confidence (HC) level. Geographic characteritics of these 305 point are described in file "Only_305_HC_points.xlsx" under the folder [CEE609_Project/Future projections/].

![305](https://user-images.githubusercontent.com/114182572/208026197-35c19075-4152-44f6-b170-b514485d1d8f.jpg)

Knowing location of our 305 points and the best GCM's, the corresponding variables of [Qair, SoilMoi, Swnet, Tair] were extracted from MIROC06-SSP245 and then used in the "Gradient_Boosting_ classification.py" [] to forecast the future fire confidence level. 

This resulted in a new extracted DataFrame called "305_Point_Future_Firemask.xlsx" which located under the folder [CEE609_Project/Future projections/]. Obtaining this DataFrame it has been used as the input of code called "Future_Fire (time_series_plot).py" and the time-series plot has been obtained in both mothly and annual basis.

[https://github.com/sbhsa1990/CEE609_Project/blob/main/Future%20projections/Future_Fire%20(time_series_plot).py]


![Untitled-10](https://user-images.githubusercontent.com/114182572/208133537-d24a3f80-ea4f-4fa9-b2e7-175ef78f6343.jpg)



