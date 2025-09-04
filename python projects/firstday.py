"""import pandas as pd
df = pd.read_csv("iris.csv")
print(df.head())
print(df.tail()

import matplotlib.pyplot as plt

x = [2021,2022,2023,2024,2025]

y= [100,200,300,400,500]
plt.xlabel('years')
plt.ylabel('sales')
plt.title('sales record')
plt.bar(x,y)
plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

plt.plot(x, 2*x+1, '-',  label='y=2x+1')   # solid
plt.plot(x, 2*x+2, '--', label='y=2x+2')   # dashed
plt.plot(x, 2*x+3, ':',  label='y=2x+3')   # dotted

plt.xlabel("x")
plt.ylabel("y")
plt.title("Graphs of y=2x+1, y=2x+2, y=2x+3")
plt.legend()
plt.grid(True)
plt.show()


