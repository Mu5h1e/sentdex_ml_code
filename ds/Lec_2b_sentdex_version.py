import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/avocado.csv')
df['Date'] = pd.to_datetime(pd['Date'])
df.set_index('Date', inplace=True)
df.sort_index(inplace=True)

Graph_DataFrame = pd.DataFrame()

for _ in set(df['regions']):
    print(_)
