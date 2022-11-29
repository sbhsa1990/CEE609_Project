# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 12:47:05 2022

@author: Babak
"""


import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split


GBC = GradientBoostingClassifier(loss='deviance', n_estimators=39,
                                 random_state=0, learning_rate=0.15,
                                 max_depth=15, min_samples_split=2,
                                 min_samples_leaf=10)

data = pd.read_excel('Inputs_dataset.xlsx')
X = data.drop(['Points', 'Fire'],1)   
y = data['Fire']


# List the input combinations
from itertools import combinations
input = X.columns
cities = sum([list(map(list, combinations(input, i))) for i in range(len(input) + 1)], [])
cities.pop(0)


# Define a DataFrame
metric_df = pd.DataFrame()

# Adding the classification libraries
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import f1_score

# Calculate the classification metrics for each of points
for city in cities:
    X_input = data[city]
    X_train, X_test, y_train, y_test = train_test_split(X_input,y,
                                                        test_size=0.25,
                                                        random_state=1)

    GBC.fit(X_train, y_train)
    GBCtest=GBC.predict(X_test)
    GBC_PS = precision_score(y_test, GBCtest, average='weighted')
    GBC_RS = recall_score(y_test, GBCtest, average='weighted')
    GBC_BAS = balanced_accuracy_score(y_test, GBCtest)
    GBC_F1 = f1_score(y_test, GBCtest, average='weighted')

    df = pd.DataFrame({'PS':[GBC_PS],'RS':[GBC_RS],'BAS':[GBC_BAS],
                       'F1':[GBC_F1]})
    metric_df = metric_df.append(df)
 
metric_df.reset_index(drop=True, inplace=True)

# Calcualte the average of each row
average_col = metric_df.mean(axis=1)
average_col = pd.DataFrame(average_col)
metric_df.insert(0, 'Mean', average_col)

# Add the number of points to the dataset
import numpy as np
p = pd.DataFrame()
p['numbers'] = np.arange(start=0, stop=len(cities), step=1, dtype=int)
p.insert(1, 'Mean', average_col)


