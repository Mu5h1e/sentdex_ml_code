import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])
albany_df = df.copy()[ df['region'] == 'Albany']
albany_df.set_index('Date', inplace=True)
albany_df.sort_index(inplace=True)
albany_df['RollingAveragePrice'] = albany_df['AveragePrice'].rolling(25).mean()
albany_df.dropna(inplace=True)
albany_df['RollingAveragePrice'].plot()
plt.show()