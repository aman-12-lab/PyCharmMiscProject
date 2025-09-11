import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

INCH_CM = 2.54
POUND_KG = 0.453592

student_data = pd.read_csv(r'C:\Users\AMANDEEP KAUR\PyCharmMiscProject\python projects\weight-height.csv')

data = student_data.to_numpy()

Length = data[:, 1]
Weight = data[:, 2]

# Convert to cm and kg
inches_to_cm = Length * INCH_CM
pounds_to_kgs = Weight * POUND_KG

# Mean values
mean_length = np.mean(inches_to_cm)
mean_weight = np.mean(pounds_to_kgs)

print("Mean Height (cm):", mean_length)
print("Mean Weight (kg):", mean_weight)

plt.hist(Length, bins=30, color="red", edgecolor="black")
plt.xlabel("Heights (inches)")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Heights")
plt.grid(True)
plt.show()