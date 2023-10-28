import pandas as pd

personas = {
    "nombre": ["Juan", "Maria", "Pedro"],
    "edad": [20, 30, 40],
    "sexo": ["M", "F", "M"],
}

df = pd.DataFrame(personas)
print(df)