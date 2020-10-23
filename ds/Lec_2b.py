import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('./datasets/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)

for _ in set(df['region'].values):
    region_df = df.copy()[df['region'] == _]
    region_df.sort_index(inplace=True)
    region_df['RollingAveragePrice'] = region_df['AveragePrice'].rolling(25).mean()
    region_df['RollingAveragePrice'].plot()

plt.show()