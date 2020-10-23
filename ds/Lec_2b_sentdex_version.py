import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/avocado.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.copy()[df['type'] == 'organic']
df.set_index('Date', inplace=True)
df.sort_values(by='Date',ascending=True,inplace=True)

Graph_DataFrame = pd.DataFrame()

for _ in set(df['region']):
    print(_)
    region_df = df.copy()[df['region'] == _]
    region_df[f'{_}_RollingAveragePrice'] = region_df['AveragePrice'].rolling(25).mean()

    if Graph_DataFrame.empty:
        Graph_DataFrame = region_df[[f'{_}_RollingAveragePrice']]
    
    else:
        Graph_DataFrame = Graph_DataFrame.join(region_df[f'{_}_RollingAveragePrice'])

Graph_DataFrame.plot()
plt.show()
print(Graph_DataFrame)
