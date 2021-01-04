import quandl
import pandas as pd

quandl.ApiConfig.api_key = 'x6xRKDkfUUycoBs-Ksn-'

df = quandl.get('WIKI/GOOGL')
print(df.head())