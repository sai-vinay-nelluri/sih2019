import pandas as pd
import numpy as np

dataset = pd.read_csv('datatest.csv')
X = dataset.iloc[:, 0:7]
Y = dataset.iloc[:, 7:]
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
X[:, 3:7] = labelencoder_X.fit_transform(X[:, 3:7])
"""X[:, 4]=labelencoder_X.fit_transform(X[:, 4])
X[:, 5]=labelencoder_X.fit_transform(X[:, 5])
X[:, 6]=labelencoder_X.fit_transform(X[:, 6])"""
onehotencoder = OneHotEncoder(categories='auto')
X = onehotencoder.fit_transform(X)
from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, Y_train)
x_pred_a = np.array(X_test[0][:]).reshape((1, -1))
Y_pred = regressor.predict(x_pred_a)
print(Y_pred)
