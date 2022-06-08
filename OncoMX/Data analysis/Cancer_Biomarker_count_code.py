#%%
# 
"""
Script to clean biomarker QCed datasets at https://data.oncomx.org for bi-weekly 
biomarker count

"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sns
plt.style.use('classic') 
sns.set(style="ticks")
# %%
# Defining a function to check for basics in the dataframe
def Dataset(dframe, valCnt = False): 
  count = 1
  print('\nDataset basic dataframe function -')
  try:
    print(f'\n{count}: Info(): ')
    count+=1
    print(dframe.info())
  except: pass

  print(f'\n{count}: Describe(): ')
  count+=1
  print(dframe.describe())
  try:
    print(f'\n{count}: Columns: ')
    count+=1
    print(dframe.columns)
  except: pass

  print(f'\n{count}: Head() -- ')
  count+=1
  print(dframe.head())

  print(f'\n{count}: Shape: ')
  count+=1
  print(dframe.shape)

  if (valCnt):
    print('\nValue Counts for each feature -')
    for colname in dframe.columns :
      print(f'\n{count}: {colname} value_counts(): ')
      print(dframe[colname].value_counts())
      count +=1

# Upload dataset using absolute pathname
df = pd.read_csv(r'/Users/hawacoulibaly/Downloads/Cancer Biomarkers v1.0 - Reviewed Biomarkers.csv' , index_col=0)

Dataset(df, True)
# %% 
# Check for Disease name column values
#df = df.rename(columns={'Disease name': 'Disease'})
#df = df.rename(columns={'BEST biomarker type': 'BEST'})
#df = df.rename(columns={'Assessed biomarker entity': 'entity'})

df['Disease name'].value_counts()
print("\nReady to continue.")
# %% 
# For the specific column, standardize disease names by replacing mispellings and other inconsistencies
df['Disease name'] = df['Disease name'].replace({'ovarian cancer (DOID: 2394)':'ovarian cancer (DOID:2394)',\
                                        'Lung cancer (DOID:1324)' : 'lung cancer (DOID:1324)',\
                                        'lung cancer (DO:1324)':'lung cancer (DOID:1324)',\
                                        'lung cancer (DO1324)':'lung cancer (DOID:1324)',\
                                        'lung cancer (DO1324)':'lung cancer (DOID:1324)',\
                                        'Breast cancer (DOID:1612)':'breast cancer (DOID:1612)', \
                                        'Prostate Cancer (DOID:10283)': 'prostate cancer (DOID:10283)',\
                                        'Prostate cancer (DOID:10283)':'prostate cancer (DOID:10283)',\
                                        'Prostate cancer (DOID: 10283)': 'prostate Cancer (DOID:10283)',\
                                        'prostate cancer ( DOID:10283)':'prostate Cancer (DOID:10283)',\
                                        'prostate Cancer (DOID:10283)':'prostate cancer (DOID:10283)',\
                                        'prostate Cancer (DOID:10283)':'prostate cancer (DOID:10283)',\
                                        'Thyroid cancer (DOID:1781)':'thyroid cancer (DOID:1781)',\
                                        'pancreatic cancer (DOID: 1793)':'pancreatic cancer (DOID:1793)', \
                                        'Head and Neck Cancer (DOID:11934)':'head and neck cancer (DOID:11934)', \
                                        'Stomach cancer (DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Stomach cancer(DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Stomach Cancer(DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Stomach cancer(DOID:10534)  ':'stomach cancer (DOID:10534)', \
                                        'Melanoma (DOID:1909)':'melanoma (DOID:1909)',\
                                        'melanoma (DOID:4159)':'melanoma (DOID:1909)',\
                                        'Liver cancer(DOID:3571)':'liver cancer (DOID:3571)',\
                                        'urinary bladder cancer (DOID: 11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Urinary bladder cancer (DOID:11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Uterine Cancer':'uterine cancer (DOID:363)',\
                                        'Kidney cancer (DOID:263)':'kidney cancer (DOID:263)',\
                                        'Kidney cancer (DOID:263) ':'kidney cancer (DOID:263)',\
                                        'esophageal cancer (DOID:5041':'esophageal cancer (DOID:5041)',\
                                        'Hepatocellular carcinoma (DOID:684)': 'liver cancer (DOID:3571)'})

print("\nReady to continue.")
# %%
# Verify that all values are standardized

print(df['Disease name'].value_counts())

print("\nReady to continue.")
# %%
# Biomarker count per disease (cancer type) : BAR CHART
from matplotlib import cm
color = cm.Blues_r(np.linspace(.4, .8, 30))
df = df.rename(columns={'Disease name': 'Disease'})
df.Disease.value_counts().plot(kind='bar', stacked=True, color=color, title='Biomarker Count per Cancer Type ', grid=False, figsize=(15,7))

print("\nReady to continue.")
# %%

