import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./datasets/minwage.csv')

minimum_wage_df = pd.DataFrame()

for name, group in df.groupby('State'):
    if minimum_wage_df.empty:
        minimum_wage_df = group.set_index('Year')[['Low.2018']].rename(columns= {'Low.2018':name})
    
    else:
        minimum_wage_df = minimum_wage_df.join(group.set_index('Year')[['Low.2018']].rename(columns={'Low.2018':name}))

minimum_wage_df.plot()
plt.show()