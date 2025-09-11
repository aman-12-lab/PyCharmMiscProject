import numpy as np
import matplotlib.pyplot as plt

for n in [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]:
    s = np.random.randint(1, 7, n) + np.random.randint(1, 7, n)
    h, h2 = np.histogram(s, range(2, 14))
    plt.bar(h2[:-1], h/n)
    plt.title(f"n = {n}")
    plt.xlabel("sum of two dice")
    plt.show()

