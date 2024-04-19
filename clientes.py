import pandas as pd
from pandas import Series, DataFrame

clientes = pd.read_excel("clientes.xlsx")

clientes.info()

clientes=clientes.fillna({'RFC':'--','NOMBRE':'--'})

print(clientes.isnull().sum())