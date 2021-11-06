# %%
import pandas as pd 

dfBionda = pd.read_csv('/Users/hawacoulibaly/Downloads/Bionda_complete.csv', index_col=0)
# Quick function check 
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

# Check
dfChkBasics(dfBionda,True)
# 
print(list(dfBionda.columns))
# %%
print(dfBionda.Disease.describe())
# %%
print(dfBionda.Disease.value_counts())
# %%
#dfBionda = dfBionda[dfBionda.Disease != ' disease']
#print(dfBionda.value_counts())
# %%
search_values = ['melanoma','stomach','thyroid','esophageal','kidney','lung','uterine','urinary','prostate','colorectal','liver','cervical','breast','brain','hematologic','head','adrenal','pancreatic','ovarian','skin' ]
dfBiondaclean = dfBionda[dfBionda['Disease'].str.contains('|'.join(search_values))]
# %% 
new_search_values = ['cancer','carcinoma','melanoma']
dfBiondacleaner = dfBiondaclean[dfBiondaclean['Disease'].str.contains('|'.join(new_search_values))]
# %%
# New Data Info

print(dfBiondacleaner['Disease'].value_counts().index.tolist())
#"display.max_rows", None)
print("\nReady to continue")
# %%
# print (dfBiondacleaner)



#%%
# create csv file for new dataframe
dfBiondacleaner.to_csv('BIONDA_Cancer_Biomarkers.csv')
# %% 
df = pd.read_csv('/Users/hawacoulibaly/Documents/GitHub/HIVE-Lab/BIONDA_Cancer_Biomarkers.csv')

# %%
for idx,name in enumerate(df['Disease'].value_counts().index.tolist()):
    print('Name :', name)
    print('Counts :', df['Disease'].value_counts()[idx])
# %%