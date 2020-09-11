import quandl 
import pandas as pd
import sklearn 
import matplotlib as plt

df = quandl.get('WIKI/GOOGL')
data_frame = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
data_frame['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']
data_frame['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
data_frame = data_frame[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]
print(data_frame)