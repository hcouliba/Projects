#%%
#from numpy.random.mtrand import f
#import matplotlib.pyplot as plt
#from matplotlib.patches import Polygon
#from pandas.core.indexing import convert_to_index_sliceable
#import seaborn as sns
#plt.style.use('classic') 
#sns.set(style="ticks")
import os
from glob import glob
import pandas as pd

# %% 
FDA_portfolio = ['dataset_breast.csv','dataset_colorectal.csv','dataset_lung.csv','dataset_melanoma.csv','dataset_ovarian.csv','dataset_prostate.csv']
#from pathlib import Path
# Path to FDA biomarker datasets folder
path = '/Users/hawacoulibaly/Documents/GitHub/HIVE-Lab/OncoMX/FDA_Dataset'
import glob
FDA_dataset = glob.glob(path + "/*.csv") # All datasets combined (melanoma, prostate, ovarian, lung, colorectal, and breast)

# %%
for i in FDA_dataset: 
        df = pd.read_csv(i, index_col=None, header=0) # Create dataframe
        for col in list(df.columns): 
                print(col,',',os.path.basename(i).replace('.csv','')) # Return column name and dataset name                
# %%

