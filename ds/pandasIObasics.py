import pandas as pd
import matplotlib as plt
import matplotlib.style as style
import quandl

style.use('ggplot')

df=quandl.get('WIKI/GOOGL')
print(df.head)