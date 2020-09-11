import quandl, math
import numpy as np
import pandas as pd
# from sklearn import preprocessing, cross_validation, svm
# from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')
data_frame = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
data_frame['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low']
data_frame['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open']
data_frame = data_frame[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'

forecast_out = int(math.ceil(0.01*len(df)))

data_frame['label'] = data_frame[forecast_col].shift(-forecast_out)
data_frame.dropna(inplace=True)

print(data_frame)