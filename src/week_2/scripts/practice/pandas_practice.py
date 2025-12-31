import pandas as pd
from pathlib import Path

# Update path to point to the repository root `data/pokemon.csv`
path = Path('data') / 'pokemon.csv'
df = pd.read_csv(path)

print(df.head())
# print("First 5 rows of the DataFrame:")
# print(df.head())

# print(f'number of rows: {df.shape[0]}')

# print("Column names:")
# for col in df.columns:
#     pass

# print(f"Data types of each column: \n{df.dtypes}")

# print("Summary statistics for numerical columns:")
# print(df.describe())

# print(df[['Name', 'Total']])

# print(df[df['Total'] > 100].to_string())

# print(df[df['Legendary'] == True])

# print(df[df['Type 1'] == 'Fire'])

# print(df[((df['Type 1'] == 'Water') & (df['Type 2'] == 'Flying')) | ((df['Type 1'] == 'Flying') & (df['Type 2'] == 'Water'))])

# print(df[(df['Type 1'] == 'Flying') & (df['Type 2'] == 'Fighting')])

# Total missing values in entire DataFrame
# print(df.isnull().sum())

# df.fillna({'Type 2': 'None'}, inplace=True)

# print(df.isnull().sum())

# df['powerful'] = df['Total'] >= 500

# # print(df[['Name', 'Total', 'powerful']])

# df['Primary_Type'] = df['Type 1']

# df.rename(columns={'powerful': 'Powerful'}, inplace=True)
# df.rename(columns={'#': 'ID'}, inplace=True)
# print(df.groupby('Type 1')['Name'].count())



print("="*60)
print("POKÉMON DATA ANALYSIS")
print("="*60)

# 4.1. Pokémon per Primary Type
print("\n1. POKÉMON PER PRIMARY TYPE:")
type_counts = df['Type 1'].value_counts()
print(type_counts)
print(f"\nTotal unique types: {len(type_counts)}")

# 4.2. Average Total for each Type 1
print("\n2. AVERAGE TOTAL FOR EACH TYPE 1:")
avg_total = df.groupby('Type 1')['Total'].mean().round(2)
print(avg_total.sort_values(ascending=False))
print(f"\nHighest average: {avg_total.idxmax()} ({avg_total.max():.1f})")
print(f"Lowest average: {avg_total.idxmin()} ({avg_total.min():.1f})")

# 4.3. Generation with highest average HP
print("\n3. GENERATION WITH HIGHEST AVERAGE HP:")
avg_hp = df.groupby('Generation')['HP'].mean().round(2)
print(avg_hp)
print(f"\nGeneration {avg_hp.idxmax()} has highest average HP: {avg_hp.max():.1f}")

# 4.4. Compare Legendary vs Non-Legendary
print("\n4. LEGENDARY VS NON-LEGENDARY COMPARISON:")
legendary_stats = df.groupby('Legendary').agg({
    'Total': 'mean',
    'HP': 'mean',
    'Attack': 'mean',
    'Defense': 'mean',
    'Sp. Atk': 'mean',
    'Sp. Def': 'mean',
    'Speed': 'mean'
}).round(2)
print(legendary_stats)

# 4.5. Strongest Pokémon in each Type 1
print("\n5. STRONGEST POKÉMON IN EACH TYPE 1:")
strongest_idx = df.groupby('Type 1')['Total'].idxmax()
strongest = df.loc[strongest_idx, ['Type 1', 'Name', 'Total', 'Legendary']]
print(strongest.sort_values('Total', ascending=False).reset_index(drop=True))

print("\n" + "="*60)
print("ANALYSIS COMPLETE")
print("="*60)

# 5.1 Finding the fastest non-legendary Pokémon
non_legendary = df[df['Legendary'] == False]
fastest_idx = non_legendary['Speed'].idxmax()
fastest_pokemon = non_legendary.loc[fastest_idx]
print("\nFASTEST NON-LEGENDARY POKÉMON:")
print(fastest_pokemon[['Name', 'Speed', 'Type 1', 'Type 2']])
