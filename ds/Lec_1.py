import pandas as pd

df = pd.read_csv('./datasets/avocado.csv')
print(df.head())
print(df["AveragePrice"].tail())
df_albany = df[df["region"]=="Albany"]
df_albany.set_index('Date',inplace=True)
print(df_albany.head())
print(df_albany.index)
