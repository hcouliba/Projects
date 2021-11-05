#%%
import os
import numpy as np
from numpy.random.mtrand import f
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sns
import glob

plt.style.use('classic') 
sns.set(style="ticks")
# %% 
# Path to FDA biomarker datasets folder
path = r'/Users/hawacoulibaly/Documents/HIVE Lab/OncoMX/Datasets/FDA_Dataset'
FDA_dataset = glob.glob(path + "/*.csv") # All datasets combined (melanoma, prostate, ovarian, lung, colorectal, and breast)

# %%
#Define parsing function to return
def parse_csv(filename):
        df = pd.read_csv(filename, index_col=None, header=0)
        for col in df.columns:
                print(col, '\n,', filename)

# %%
# Apply function to dataset
for x in FDA_dataset:
        print(parse_csv(x))

# ##