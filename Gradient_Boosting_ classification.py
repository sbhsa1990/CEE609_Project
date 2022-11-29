# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 13:12:46 2021

@author: Babak Asadollah
"""


import numpy as np
import pandas as pd
from sklearn import ensemble
from sklearn.model_selection import train_test_split

# Import Dataset
data = pd.read_excel('Inputs.xlsx')

# Drop the unwanted columns
X = data.drop(['Points','Fire'],1)

# Define the target variable
y = data['Fire']

# Split DataSet to Train & Test
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.25,
                                                    random_state=0)


from sklearn.ensemble import GradientBoostingClassifier

GBC = GradientBoostingClassifier(loss='deviance', n_estimators=39,
                                     random_state=0, learning_rate=0.15,
                                     max_depth=15, min_samples_split=2,
                                     min_samples_leaf=10)

GBC.fit(X_train, y_train)
GBCtest=GBC.predict(X_test)
GBCperform1=GBC.score(X_test, y_test)
A = abs(GBCperform1)




