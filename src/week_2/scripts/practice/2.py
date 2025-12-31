import pandas as pd
from pathlib import Path

path = Path('data') / 'pokemon.csv'

df = pd.read_csv(path)

# print(df.groupby('Type 1')['Name'].count())

# print(df['Total'].idxmax())
# print(df.iloc[163])

print(df.loc[df['Total'].idxmax()])