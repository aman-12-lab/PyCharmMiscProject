import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, Lasso
from sklearn.preprocessing import StandardScaler


df = pd.read_csv("Auto.csv")

X = df.drop(columns=["mpg", "name", "origin"])
y = df["mpg"]

X = StandardScaler().fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

alphas = np.logspace(-3, 3, 20)
ridge_scores, lasso_scores = [], []

for a in alphas:
    ridge = Ridge(alpha=a).fit(X_train, y_train)
    lasso = Lasso(alpha=a, max_iter=10000).fit(X_train, y_train)
    ridge_scores.append(ridge.score(X_test, y_test))
    lasso_scores.append(lasso.score(X_test, y_test))

plt.semilogx(alphas, ridge_scores, label="Ridge")
plt.semilogx(alphas, lasso_scores, label="Lasso")
plt.xlabel("alpha")
plt.ylabel("R2")
plt.legend()
plt.show()

best_ridge_alpha = alphas[np.argmax(ridge_scores)]
best_lasso_alpha = alphas[np.argmax(lasso_scores)]
print("Best Ridge alpha:", best_ridge_alpha)
print("Best Lasso alpha:", best_lasso_alpha)

"""
- Ridge usually gives smoother improvement and resists overfitting.
- Lasso may drop some variables completely (feature selection).
- The best alpha is the one with the highest R2 on the test set (printed above).
"""
