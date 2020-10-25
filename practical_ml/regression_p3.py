import pandas as pd 
import quandl
import math 

q_df = quandl.get('WIKI/GOOGL')
df = pd.DataFrame()
df = q_df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
df = df.copy()[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

df['label'] = df['Adj. Close'].shift(-int(math.ceil(0.01*len(df))))

print(df.head())
