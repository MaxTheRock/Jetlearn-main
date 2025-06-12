import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

boston_data = pd.read_csv("boston_house_prices.csv")
boston = pd.DataFrame(boston_data)

print(boston.head())

#boston["MEDV"] = boston_data.target

x = boston[["LSTAT","RM"]]
y = boston["MEDV"]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=5)

from sklearn.linear_model import LinearRegression

model1 = LinearRegression()
model1.fit(x_train,y_train)

from sklearn.metrics import mean_squared_error

y_predict = model1.predict(x_test)

rm_model1 = (np.sqrt(mean_squared_error(y_test,y_predict)))

print(rm_model1)