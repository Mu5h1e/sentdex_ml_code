import quandl
import pandas as pd 

df = quandl.get('WIKI/GOOGL')
info_df = pd.DataFrame()
info_df = df
info_df = info_df.copy()[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
info_df['HL_PCT'] = (info_df['Adj. High'] - info_df['Adj. Close']) / info_df['Adj. Close'] * 100
info_df['PCT_CHANGE'] = (info_df['Adj. Close'] - info_df['Adj. Open']) / info_df['Adj. Open'] * 100

info_df = info_df.copy()[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]
print(info_df.head())