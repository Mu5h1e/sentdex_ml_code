import quandl
import pandas as pd 

df = quandl.get('WIKI/GOOGL')
info_df = pd.DataFrame()
info_df = df
info_df = info_df.copy()[['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
print(info_df.description)