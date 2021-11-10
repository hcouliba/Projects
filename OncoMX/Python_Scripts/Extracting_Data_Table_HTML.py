# %%
# Importing pandas
import pandas as pd
from bs4 import BeautifulSoup
# 
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
  
# The webpage URL whose table we want to extract
url = "https://data.oncomx.org/cancerbiomarkers"
  
# Assign the table data to a Pandas dataframe
table = pd.read_html(url)[0]
# %%
# Store the dataframe in Excel file
table.to_csv("data.xlsx")
# %%