# %%
# Import modules 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import seaborn as sns
plt.style.use('classic') 
sns.set(style="ticks")
# %%
df = pd.read_csv(r'/Users/hawacoulibaly/Documents/HIVE Lab/FDA-OncoMX/FDA_NABT.csv') 

# %%
from matplotlib import cm

color = cm.inferno_r(np.linspace(.4, .8, 30))
df.Use.value_counts().plot(kind='bar', stacked=True, color=color, title='Biomarker Count per Use ', grid=False, figsize=(15,7))
# %%
dubc = df.groupby('Use').Measurand.nunique()
UniqueCount = pd.DataFrame({'Use':dubc.index, 'Unique_count':dubc.values})

U
# %% 
# Draw plot
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(16,10), facecolor='white', dpi= 80)
ax.vlines(x=UniqueCount.index, ymin=0, ymax=UniqueCount.Unique_count, color='firebrick', alpha=0.7, linewidth=20)

# Annotate Text
for i, Unique_count in enumerate(UniqueCount.Unique_count):
    ax.text(i, Unique_count+0.5, round(Unique_count, 1), horizontalalignment='center')


# Title, Label, Ticks and Ylim
ax.set_title('Bar Chart for Highway Mileage', fontdict={'size':22})
ax.set(ylabel='Miles Per Gallon', ylim=(0, 30))
plt.xticks(UniqueCount.index, UniqueCount.Use.str.upper(), rotation=60, horizontalalignment='right', fontsize=12)

# Add patches to color the X axis labels
p1 = patches.Rectangle((.57, -0.005), width=.33, height=.13, alpha=.1, facecolor='green', transform=fig.transFigure)
p2 = patches.Rectangle((.124, -0.005), width=.446, height=.13, alpha=.1, facecolor='red', transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)
plt.show()
# %%
fig, ax = plt.subplots(figsize=(16,10), dpi= 80)
ax.vlines(x=UniqueCount.index, ymin=0, ymax=UniqueCount.Unique_count, color='firebrick', alpha=0.7, linewidth=2)
ax.scatter(x=UniqueCount.index, y=UniqueCount.Unique_count, s=75, color='firebrick', alpha=0.7)

# Title, Label, Ticks and Ylim
ax.set_title('Unique biomarkers per Use', fontdict={'size':22})
ax.set_ylabel('Unique biomarker count per Use')
ax.set_xticks(UniqueCount.index)
ax.set_xticklabels(UniqueCount.Use.str.upper(), rotation=90, fontdict={'horizontalalignment': 'right', 'size':12})
ax.set_ylim(0, 30)

# Annotate
for row in UniqueCount.itertuples():
    ax.text(row.Index, row.Unique_count+.5, s=round(row.Unique_count, 2), horizontalalignment= 'center', verticalalignment='bottom', fontsize=14)

plt.show()
# %%
