import pandas as pd
from pandas import DataFrame
import numpy as np
import os
import re
import statistics 
import scipy
from scipy.stats import zscore
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

#read in all the gene distributions
HEAVY=pd.read_csv('HC-VJ.csv')
KAPPA=pd.read_csv('LC-VJ-kappa.csv')
LAMBDA=pd.read_csv('LC-VJ-lambda.csv')

HEAVY.head(5)

HEAVY_in=HEAVY.set_index('V')
KAPPA_in=KAPPA.set_index('V')
LAMBDA_in=LAMBDA.set_index('V')


HEAVY_in.head(5)

fig, (ax1) = plt.subplots(1, 1, sharex=False, sharey=True, figsize = (160,30))
sns.set(font_scale=2.0)

sns.heatmap(HEAVY_in, vmin = -10, vmax= 20, cmap='coolwarm', robust=True, square=True, linewidths=2.0, cbar= True, annot=True, annot_kws={"size": 20}, cbar_kws={"fraction": 0.15, "shrink":1.0, "aspect":60}, ax=ax1)

fig.tight_layout()

plt.show()

fig.savefig('heatmapsHC.png')


fig, (ax1, ax2) = plt.subplots(1, 2, sharex=False, sharey=False, figsize = (160,30))
sns.set(font_scale=2.0)

sns.heatmap(LAMBDA_in, vmin = -10, vmax= 20, cmap='coolwarm', robust=True, square=True, linewidths=2.0, cbar= False, annot=True, annot_kws={"size": 30}, ax=ax1)
sns.heatmap(KAPPA_in, vmin = -10, vmax= 20, cmap='coolwarm', robust=True, square=True, linewidths=2.0, cbar= True, annot=True, annot_kws={"size": 30}, cbar_kws={"fraction": 0.15, "shrink":1.0, "aspect":60}, ax=ax2)

fig.tight_layout()

plt.show()

fig.savefig('heatmapsLIGHTS.png')
