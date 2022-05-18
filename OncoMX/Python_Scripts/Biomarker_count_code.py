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
df = pd.read_csv(r'/Users/hawacoulibaly/Desktop/All_FDA.csv' , index_col=0) 
dfChkBasics(df, True)
#%%
df = df.rename(columns={'Disease name': 'Disease'})
df = df.rename(columns={'BEST biomarker type': 'BEST'})
df = df.rename(columns={'Assessed biomarker entity': 'entity'})

#df['Disease'].value_counts()
#df['BEST biomarker type'].value_counts()

# %%
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
                                        'prostate Cancer (DOID:10283)':'prostate cancer (DOID:10283)',\
                                        'Thyroid cancer (DOID:1781)':'thyroid cancer (DOID:1781)',\
                                        'pancreatic cancer (DOID: 1793)':'pancreatic cancer (DOID:1793)', \
                                        'Head and Neck Cancer (DOID:11934)':'head and neck cancer (DOID:11934)', \
                                        'Stomach cancer (DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Stomach cancer(DOID:10534)':'stomach cancer (DOID:10534)', \
                                        'Melanoma (DOID:1909)':'melanoma (DOID:1909)',\
                                        'melanoma (DOID:4159)':'melanoma (DOID:1909)',\
                                        'Liver cancer(DOID:3571)':'liver cancer (DOID:3571)',\
                                        'urinary bladder cancer (DOID: 11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Urinary bladder cancer (DOID:11054)':'urinary bladder cancer (DOID:11054)',\
                                        'Uterine Cancer':'uterine cancer (DOID:363)',\
                                        'Kidney cancer (DOID:263)':'kidney cancer (DOID:263)',\
                                        'Hepatocellular carcinoma (DOID:684)': 'liver cancer (DOID:3571)'})

# %%
print(df.Disease.describe(), '\n', df.Disease.value_counts(dropna=False))

# %%
from matplotlib import cm
color = cm.Blues_r(np.linspace(.4, .8, 30))
df.Disease.value_counts().plot(kind='bar', stacked=True, color=color, title='Biomarker Count per Cancer Type ', grid=False, figsize=(15,7))
# %%
#%%
from matplotlib import cm
color = cm.inferno_r(np.linspace(.4, .8, 30))
df.Disease.value_counts().plot(kind='bar', stacked=True, color=color, title='Biomarker Count per Cancer Type ', grid=False, figsize=(15,7))
# %% 
# Count total number of rows 
index = df.index
number_of_rows = len(index)
print(number_of_rows)
# %%
print(df.nunique())
# %%
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Use the venn2 function
venn2(subsets = (258, 0, 213), set_labels = ('', ''))
plt.show()
# %%
df = pd.read_csv(r'/Users/hawacoulibaly/Downloads/Cancer Biomarkers v1.0 - Reviewed Biomarkers.csv' , index_col=0)
df = df.rename(columns={'Disease name': 'Disease'})
index = df.index
number_of_rows = len(index)
print(number_of_rows)
# %%
print(df.nunique())


# %%
# Prepare data
x_var = 'Disease'
groupby_var = 'BEST'
df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
vals = [df[x_var].values.tolist() for i, df in df_agg]

# Draw
plt.figure(figsize=(16,9), dpi= 80)
colors = [plt.cm.Spectral(i/float(len(vals)-1)) for i in range(len(vals))]
n, bins, patches = plt.hist(vals, df[x_var].unique().__len__(), stacked=True, density=False, color=colors[:len(vals)])

# Decoration
plt.legend({group:col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
plt.title(f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$", fontsize=22)
plt.xlabel(x_var)
plt.ylabel("Frequency")
plt.ylim(0, 200)
plt.xticks(ticks=bins, labels=np.unique(df[x_var]).tolist(), rotation=90, horizontalalignment='left')
plt.show()
# %%
