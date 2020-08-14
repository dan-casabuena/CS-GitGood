import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

dataset = pd.read_csv('players.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values
AvgDistance = dataset.iloc[:, 2:3].values
Aces = dataset.iloc[:, 3:4].values
cat = np.concatenate((Aces, y.reshape(-1, 1)), axis=1)
ordered_cat = cat[np.argsort(cat[:, 0])]

ace_data = []
ls = []
index = 0
for elem in ordered_cat:
    if elem[0] != index:
        index += 1
        ace_data.append(ls)
        ls = []
    ls.append(elem[1])


X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()

AvgDistance2 = sm.add_constant(AvgDistance)
est_dist = sm.OLS(y, AvgDistance2)
est_dist2 = est_dist.fit()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

distance_reg = LinearRegression()
distance_reg.fit(AvgDistance, y)

# Predicting the test set results
y_pred = regressor.predict(X_test)
# print the y_pred

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Head Shot Ratio vs KDA Ratio')
plt.xlabel('Headshot Ratio')
plt.ylabel('KDA Ratio')
plt.show()
est2.summary()

plt.scatter(AvgDistance, y, color='red')
plt.plot(AvgDistance, distance_reg.predict(AvgDistance), color='blue')
plt.title('Average Distance of Kills vs KDA Ratio')
plt.xlabel('Average Distance of Kills')
plt.ylabel('KDA Ratio')
plt.show()
est_dist2.summary()

plt.boxplot(ace_data)
plt.title('Aces vs KDA Ratio')
plt.xlabel('Aces')
plt.ylabel('KDA Ratio')
plt.show()
