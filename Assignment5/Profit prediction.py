import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("50_Startups.csv")
print(df)

"""
Typical columns are: R&D Spend, Administration, Marketing Spend, State, Profit
- Profit is the target variable
- State is categorical 
- Other columns are numeric explanatory variables.
"""

print("Columns:", df.columns.tolist())

# 2) Investigate correlation between variables
corr = df.corr(numeric_only=True)
print("Correlation matrix:\n", corr)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.scatter(df['R&D Spend'], df['Profit'])
plt.xlabel('R&D Spend')
plt.ylabel('Profit')


plt.subplot(1,2,2)
plt.scatter(df['Marketing Spend'], df['Profit'])
plt.xlabel('Marketing Spend')
plt.ylabel('Profit')
plt.tight_layout()
plt.show()

X = df[["R&D Spend", "Marketing Spend"]]
y = df["Profit"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
rmse_train = np.sqrt(mean_squared_error(y_train, train_pred))
r2_train = r2_score(y_train, train_pred)

test_pred = model.predict(X_test)
rmse_test = np.sqrt(mean_squared_error(y_test, test_pred))
r2_test = r2_score(y_test, test_pred)

print("Training RMSE=", rmse_train, "R2=", r2_train)
print("Testing RMSE=", rmse_test, "R2=", r2_test)

"""
- R&D Spend shows the strongest linear relationship with Profit.
- Marketing Spend also helps improve predictions, though weaker.
- Model achieves low RMSE and good R², especially on training data.
- Administration and State did not provide much predictive power.
"""
