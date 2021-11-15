# %% 
import requests
url = 'https://www.fda.gov/medical-devices/in-vitro-diagnostics/list-cleared-or-approved-companion-diagnostic-devices-in-vitro-and-imaging-tools'
FDApage = requests.get(url)
print(FDApage.status_code)

# %%
from bs4 import BeautifulSoup
soup = BeautifulSoup(FDApage.content, 'html5lib')
table = soup.find_all('table')[0] # Grab the first table
import pandas as pd
df = pd.read_html(str(table))[0]
df.to_csv('whaever.csv') # I know the size 
# %%
    