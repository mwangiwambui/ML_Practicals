# import codecademylib3_seaborn
# Assuming i have a file that has the height and weight of baseball players, we want to find the avg height and
# weight of a baseball player
from GradientDescentforSlope import gradient_descent
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("heights.csv")

X = df["height"]
y = df["weight"]
b,m = gradient_descent(X,y,0.0001,1000)
y_predictions = [x*m + b for x in X]
plt.plot(X, y, 'o')
#plot your line here:
plt.plot(X,y_predictions)
plt.show()