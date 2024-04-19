import pandas as pd
from pandas import Series, DataFrame

precios_productos = pd.read_excel("precios_productos.xlsx")

precios_productos.info()

print(precios_productos.isnull().sum())