import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import pickle

df = quandl.get('WIKI/GOOGL')
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']
df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]
forecast_col = 'Adj. Close'
df.fillna(-99999, inplace = True)
forecase_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecase_out)
df.dropna(inplace = True)

x = np.array(df.drop(['label'],1))
x = preprocessing.scale(x)
y = np.array(df['label'])
print 'HERE'

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)
with open('linearregression.pickle','wb') as f:
    pickle.dump(clf,f)
pickle_in = open('linearregression.pickle','rb')
clf1 = pickle.load(pickle_in)
accuracy1 = clf1.score(x_test, y_test)
print 'linear regression accuracy: ',accuracy1

# clf2 = svm.SVR()
# clf2.fit(x_train, y_train)
# accuracy2 = clf2.score(x_test, y_test)
# print 'SVM accuracy: ',accuracy2
