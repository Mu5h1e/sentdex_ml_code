import pandas as pd
import matplotlib as plt
import matplotlib.style as style
style.use('ggplot')
# pandas is fast thats the scene 

web_stats = {
            'Day':[1,2,3,4,5,6],
            'Visitors':[43, 53, 34, 45, 64, 34],
            'Bounce_rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
print(df)
print(df.head())
print(df.tail())
print(df.tail(2))
