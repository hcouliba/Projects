# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sns
plt.style.use('classic') 
sns.set(style="ticks")

def dfChkBasics(dframe, valCnt = False): 
  cnt = 1
  print('\ndataframe Basic Check function -')
  try:
    print(f'\n{cnt}: info(): ')
    cnt+=1
    print(dframe.info())
  except: pass

  print(f'\n{cnt}: describe(): ')
  cnt+=1
  print(dframe.describe())
  try:
    print(f'\n{cnt}: columns: ')
    cnt+=1
    print(dframe.columns)
  except: pass

  print(f'\n{cnt}: head() -- ')
  cnt+=1
  print(dframe.head())

  print(f'\n{cnt}: shape: ')
  cnt+=1
  print(dframe.shape)

  if (valCnt):
    print('\nValue Counts for each feature -')
    for colname in dframe.columns :
      print(f'\n{cnt}: {colname} value_counts(): ')
      print(dframe[colname].value_counts())
      cnt +=1
df = pd.read_csv(r'/Users/hawacoulibaly/Downloads/Cancer Biomarkers v1.0 - QCed Reviewed Biomarkers-4.csv' , index_col=0) 
dfChkBasics(df, True)
print(df.Disease.describe(), '\n', df.Disease.value_counts(dropna=False))

print("\nReady to continue.")
# %% 
df['Disease'] = df['Disease'].replace({'ovarian cancer (DOID: 2394)':'ovarian cancer (DOID:2394)',\
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
                                        'Thyroid cancer (DOID:1781)':'thyroid cancer (DOID:1781)',\
                                        'pancreatic cancer (DOID: 1793)':'pancreatic cancer (DOID:1793)', \
                                        'Head and Neck Cancer (DOID:11934)':'head and neck cancer (DOID:11934)', \
                                        'Stomach cancer (DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Melanoma (DOID:1909)':'melanoma (DOID:1909)',\
                                        'melanoma (DOID:4159)':'melanoma (DOID:1909)',\
                                        'urinary bladder cancer (DOID: 11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Urinary bladder cancer (DOID:11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Uterine Cancer':'uterine cancer (DOID:363)',\
                                        'Kidney cancer (DOID:263)':'kidney cancer (DOID:263)',\
                                        'Hepatocellular carcinoma (DOID:684)': 'liver cancer (DOID:3571)'})

# %%

df.Disease.value_counts().plot(kind='bar', title='Biomarker Count per Cancer Type ', grid=False, figsize=(15,7))
# %%


# %%
