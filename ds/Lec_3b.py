import pandas as pd 
import matplotlib.pyplot as plt  
import numpy as np 

df = pd.read_csv('./datasets/minwage.csv')
df.set_index('Year', inplace=True)

minwage_df = pd.DataFrame()

for name, group in df.groupby('State'):
    if minwage_df.empty:
        minwage_df = group[['Low.2018']].rename(columns={'Low.2018':name})
    
    else:
        minwage_df = minwage_df.join(group[['Low.2018']].rename(columns={'Low.2018':name}))

minwage_df = minwage_df.replace(0, np.NaN).dropna(axis=1)

minwage_df.plot()
plt.show()