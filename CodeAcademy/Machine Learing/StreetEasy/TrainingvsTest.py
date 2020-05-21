# import codecademylib3_seaborn
import pandas as pd
import matplotlib.pyplot as plt
# used to split the data to a training set and a test set
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# import train_test_split

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/manhattan.csv")
df = pd.DataFrame(streeteasy)
x = df[['bedrooms','bathrooms','size_sqft','min_to_subway','floor','building_age_yrs', 'no_fee','has_roofdeck','has_washer_dryer','has_doorman'
,'has_elevator','has_dishwasher','has_patio','has_gym']]
y = df[['rent']]
x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2, random_state = 6)
print(x_train.shape)
print(x_test.shape)

print(y_train.shape)
print(y_test.shape)

# till here we picked the training set and the test set

# Add the code here:


mlr = LinearRegression()
mlr.fit(x_train, y_train)
# predicting sonia appartment
y_predict = mlr.predict(x_test)

# score is used to calculate the loss
print(mlr.score(x_train,y_train))
# sonny_apartment = [[1, 1, 620, 16, 1, 98, 1, 0, 1, 0, 0, 1, 1, 0]]
# predict = mlr.predict(sonny_apartment)
#
# print("Predicted rent: $%.2f" % predict)

# The alpha parameter is added to better understand overlapping of points (0.0 transparent - 1.0 opaque).
plt.scatter(y_test, y_predict, alpha=0.4)
plt.xlabel("Prices: $Y_i$")
plt.ylabel("Predicted prices: $\hat{Y}_i$")
plt.title("Actual Rent vs Predicted Rent")
plt.show()

