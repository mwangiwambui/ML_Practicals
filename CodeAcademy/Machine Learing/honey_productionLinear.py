# import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")
print(df.head())
# Use the .groupby() method provided by pandas to get the mean of totalprod per year.
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
# select a column from a DataFrame by using bracket notation:
X = df["year"]
# reshaping to get into the right format
X = X.values.reshape(-1, 1)

y = df["totalprod"]
# To plot a scatterplot,
plt.scatter(X,y)

regr = linear_model.LinearRegression()
regr.fit(X,y)
# print slope
print(regr.coef_[0])
# print intercept
print(regr.intercept_)
y_predict = regr.predict(X)
plt.plot(X, y_predict)


# So, it looks like the production of honey has been in decline, according to this linear model. Let’s predict what the year 2050 may look like in terms of honey production.
# The code below makes a NumPy array with the numbers 1 through 10
X_future = np.array(range(2013, 2050))
# After creating that array, we need to reshape it for scikit-learn.
X_future = X_future.reshape(-1, 1)
# The above makes it a column instead of one big row.
future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()
