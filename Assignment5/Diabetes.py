import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


data = load_diabetes(as_frame=True)
df = data['frame']


plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.scatter(df['bmi'], df['target'], alpha=0.6,)
plt.xlabel('bmi')
plt.ylabel('target')
plt.title("BMI vs Target")

plt.subplot(1,2,2)
plt.scatter(df['s5'], df['target'], alpha=0.6,)
plt.xlabel('s5')
plt.ylabel('target')
plt.title("S5 vs Target")

plt.tight_layout()
plt.show()


X = df[['bmi', 's5']]
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)


y_train_pred = model.predict(X_train)
rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
r2_train = r2_score(y_train, y_train_pred)

y_test_pred = model.predict(X_test)
rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
r2_test = r2_score(y_test, y_test_pred)

print(f"Training: RMSE={rmse_train:.2f}, R²={r2_train:.2f}")
print(f"Testing : RMSE={rmse_test:.2f}, R²={r2_test:.2f}")

plt.scatter(y_test, y_test_pred, color="teal", alpha=0.7)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted (Test Data)")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')
plt.show()



