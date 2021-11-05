#%%
# Open and read FDA Human Breast cancer biomarker dataset
import pandas as pd 
fh = pd.read_csv('Human_cancer_biomarkers_FDA_breast.csv')

# Print field names (column names)
for col in fh.columns: 
    print(col)
#%%
import pandas as pd
fh = pd.read_csv('https://example.com/passkey=wedsmdjsjmdd')