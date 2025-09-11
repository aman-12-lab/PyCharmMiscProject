import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

data = pd.read_csv("weight-height.csv")
X = data[["Height"]]
y = data["Weight"]

plt.scatter(X,y)
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()

regr = LinearRegression()

regr.fit(X, y)

plt.scatter(X, y)
plt.plot(X, regr.predict(X))
plt.title("Linear Regression: Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.legend()
plt.show()

y_pred = regr.predict(X)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"RMSE: {rmse:.2f}")
print(f"R2: {r2:.3f}")



