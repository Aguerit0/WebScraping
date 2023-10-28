import pandas as pd

df = pd.read_csv('https://docs.google.com/spreadsheets/d/1BA8IP2VsCZAQ2MMxq1twrindVGMU7JHe4Qrdn-8N9Oc/export?format=csv&gid=2056133412')

# Ejemplo de filtrado
print(df.sample(20))

#Datos estadísticos del dataFrame
print(df.describe())

# Matplotlib para graficar
import matplotlib.pyplot as plt
df.plot.scatter(x='Edad', y='Peso', title='Peso vs Edad')
plt.show()

#Altura vs Peso
df.plot.scatter(x='Altura', y='Peso', title='Altura vs Edad')
plt.show()

