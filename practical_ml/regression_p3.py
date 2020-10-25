import pandas as pd 
import quandl, math
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression
import numpy as np

q_df = quandl.get('WIKI/GOOGL')
df = pd.DataFrame()
df = q_df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100
df = df.copy()[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

df['label'] = df['Adj. Close'].shift(-int(math.ceil(0.01*len(df))))
df.dropna(inplace=True)

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])

x = preprocessing.scale(x)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

classifier = LinearRegression()
classifier.fit(x_train, y_train)
accuracy = classifier.score(x_test, y_test)

print(f'{accuracy*100}% accuracy')