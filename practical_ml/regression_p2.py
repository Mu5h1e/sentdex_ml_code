import quandl
import pandas as pd 
import math

df = quandl.get('WIKI/GOOGL')
goog_info_df = pd.DataFrame()
goog_info_df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
goog_info_df['HL_PCT'] = (goog_info_df['Adj. High'] - goog_info_df['Adj. Close']) / goog_info_df['Adj. Close'] * 100
goog_info_df['PCT_CHANGE'] = (goog_info_df['Adj. Close'] - goog_info_df['Adj. Open']) / goog_info_df['Adj. Open'] * 100
goog_info_df = goog_info_df.copy()[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forecast_col = 'Adj. Close'

goog_info_df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(goog_info_df)))

goog_info_df['label'] = goog_info_df[forecast_col].shift(-forecast_out)
goog_info_df.dropna(inplace=True)
print(goog_info_df.head())