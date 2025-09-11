import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])


y1 = 2*x + 1
y2 = 2*x + 2
y3 = 2*x + 3

plt.plot(x, y1,  label="y = 2x + 1")
plt.plot(x, y2,  label="y = 2x + 2")
plt.plot(x, y3,  label="y = 2x + 3")

plt.title("scatter plot of points")
plt.xlabel("x-axis")
plt.ylabel("y-axis")


plt.legend()
plt.grid(True)

plt.show()

