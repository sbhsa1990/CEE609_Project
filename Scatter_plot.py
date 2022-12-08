
"""
@author: Babak Asadollah
"""

import numpy as np
import pandas as pd  
from matplotlib import pyplot as plt

import matplotlib as mpl
mpl.rcParams['figure.figsize'] = 6, 6
mpl.rcParams['xtick.major.size'] = 10
mpl.rcParams['xtick.major.width'] = 2
mpl.rcParams['ytick.major.pad']='5'
mpl.rcParams['ytick.major.size'] = 10
mpl.rcParams['ytick.major.width'] = 2
mpl.rcParams['axes.linewidth'] = 2
plt.rcParams.update({'font.family':'Times New Roman'})

data = pd.read_excel('rsds.xlsx')
X = data.drop(['Target'],1)
x = pd.DataFrame(X)
Y = data['Target']
y = pd.DataFrame(Y)

for col in x.columns:
    X1= data[[col]]
	X1 = pd.DataFrame(X1)
  	concatDF = pd.concat((X1,y),axis=1)
	concatDF.columns=['yhat', 'y_test']
	column_1 = concatDF["y_test"]
	column_2 = concatDF["yhat"]
	R = column_1.corr(column_2)
	R_sqrd = abs(A)**2  

	plt.scatter(y, X1,  s=50, c='Red', linewidths=0.75, edgecolors='Black', vmax=400)
	plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
	plt.xticks(np.arange(0, 310, 50), fontsize=16)
	plt.yticks(np.arange(0, 450, 50), fontsize=16)
	plt.title(col, fontsize=20, fontweight="bold", pad=10)
	plt.xlabel('Observed products', fontsize=20, fontweight="bold", labelpad=10)
	plt.ylabel('Simulated products', fontsize=20, fontweight="bold", labelpad=10)
	plt.annotate("R-squared = {:.3f}".format(A), (10, 350), fontsize = 18, fontweight="bold")



	fig1 = plt.gcf()
	plt.show()
	plt.draw()
	plt.tight_layout()
	fig1.savefig(col + '.png', dpi=300, bbox_inches='tight')

