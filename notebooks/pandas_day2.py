import pandas as pd
import numpy as np

data = pd.read_csv('titanic.csv')
df = pd.DataFrame(data)

# print(df)

# print(df.shape)
# print(df.info())
# print(df.describe())

df = df.fillna(df.mean(numeric_only=True))
df = df.fillna('Unknown')

# print(df)

grouped = df.groupby('Pclass')
# print(df.groupby('Pclass').size())

print(df.columns)