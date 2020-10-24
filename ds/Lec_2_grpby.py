import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/avocado.csv', engine='python')
df = df.copy()[df['type'] == 'organic']
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date',inplace=True)
df.sort_index(inplace=True)

avocado_avg_price_df = pd.DataFrame()

for name, group in df.groupby('region'):
    group['Rolling25Ma']=group['AveragePrice'].rolling(25).mean()
    if avocado_avg_price_df.empty:
        avocado_avg_price_df = group[['Rolling25Ma']].rename(columns={'Rolling25Ma':name})
    else:
        avocado_avg_price_df = avocado_avg_price_df.join(group[['Rolling25Ma']].rename(columns={'Rolling25Ma':name}))

avocado_avg_price_df.plot()
plt.show()

