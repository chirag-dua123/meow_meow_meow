import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
path = Path('data') / 'pokemon.csv'
df = pd.read_csv(path)

# 2. Display first 5 rows
print("First 5 rows:")
print(df.head())
print("\n" + "="*50 + "\n")

# 3. How many Pokémon are in the dataset?
print(f"Total Pokémon in dataset: {len(df)}")
print("\n" + "="*50 + "\n")

# 4. What are the column names?
print("Column names:")
print(df.columns.tolist())
print("\n" + "="*50 + "\n")

# 5. Show data types of each column
print("Data types:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

# 6. Display basic statistics for numeric columns
print("Basic statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# 1. Select only 'Name' and 'Total' columns
name_total = df[['Name', 'Total']]
print("Name and Total columns (first 10):")
print(name_total.head(10))
print("\n" + "="*50 + "\n")

# 2. Find all Pokémon with HP > 100
high_hp = df[df['HP'] > 100]
print(f"Pokémon with HP > 100 ({len(high_hp)} found):")
print(high_hp[['Name', 'HP']].head(10))
print("\n" + "="*50 + "\n")

# 3. Find all Legendary Pokémon
legendary = df[df['Legendary'] == True]
print(f"Legendary Pokémon ({len(legendary)} found):")
print(legendary[['Name', 'Type 1', 'Type 2', 'Total']].head(10))
print("\n" + "="*50 + "\n")

# 4. Get all Fire-type Pokémon (in Type 1)
fire_types = df[df['Type 1'] == 'Fire']
print(f"Fire-type Pokémon ({len(fire_types)} found):")
print(fire_types[['Name', 'Type 2', 'Total']].head(10))
print("\n" + "="*50 + "\n")

# 5. Find Pokémon that are both Water and Flying
water_flying = df[(df['Type 1'] == 'Water') & (df['Type 2'] == 'Flying')]
print(f"Water/Flying Pokémon ({len(water_flying)} found):")
print(water_flying[['Name', 'Total']])

# 1. How many missing values in each column?
print("Missing values per column:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")

# 2. Fill missing values in Type 2 with 'None'
df['Type 2'] = df['Type 2'].fillna('None')
print("Type 2 missing values after filling:\n", df['Type 2'].isnull().sum())
print("\n" + "="*50 + "\n")

# 3. Create 'Powerful' column
df['Powerful'] = df['Total'] > 500
print("Powerful Pokémon (Total > 500):")
print(df[df['Powerful']][['Name', 'Total', 'Powerful']].head(10))
print("\n" + "="*50 + "\n")

# 4. Create 'Primary_Type' column
df['Primary_Type'] = df['Type 1']
print("Primary Type column created")
print(df[['Name', 'Primary_Type']].head(10))
print("\n" + "="*50 + "\n")

# 5. Rename column # to ID
df = df.rename(columns={'#': 'ID'})
print("Renamed # column to ID")
print(df.columns.tolist())

# 1. How many Pokémon per Primary Type?
type_counts = df['Type 1'].value_counts()
print("Pokémon per Primary Type:")
print(type_counts)
print("\n" + "="*50 + "\n")

# 2. Average Total for each Type 1
avg_total_by_type = df.groupby('Type 1')['Total'].mean().sort_values(ascending=False)
print("Average Total by Type 1:")
print(avg_total_by_type)
print("\n" + "="*50 + "\n")

# 3. Which Generation has highest average HP?
avg_hp_by_gen = df.groupby('Generation')['HP'].mean()
print("Average HP by Generation:")
print(avg_hp_by_gen)
print(f"\nGeneration with highest average HP: {avg_hp_by_gen.idxmax()} ({avg_hp_by_gen.max():.1f})")
print("\n" + "="*50 + "\n")

# 4. Compare average stats of Legendary vs Non-Legendary
legendary_stats = df.groupby('Legendary').agg({
    'HP': 'mean',
    'Attack': 'mean',
    'Defense': 'mean',
    'Sp. Atk': 'mean',
    'Sp. Def': 'mean',
    'Speed': 'mean',
    'Total': 'mean'
}).round(1)
print("Average stats - Legendary vs Non-Legendary:")
print(legendary_stats)
print("\n" + "="*50 + "\n")

# 5. Find strongest Pokémon in each Type 1
strongest_by_type = df.loc[df.groupby('Type 1')['Total'].idxmax()]
print("Strongest Pokémon in each Type 1:")
print(strongest_by_type[['Type 1', 'Name', 'Total']].sort_values('Total', ascending=False))

# 1. Fastest non-Legendary Pokémon
non_legendary = df[df['Legendary'] == False]
fastest_non_legendary = non_legendary.loc[non_legendary['Speed'].idxmax()]
print("Fastest non-Legendary Pokémon:")
print(f"Name: {fastest_non_legendary['Name']}")
print(f"Speed: {fastest_non_legendary['Speed']}")
print(f"Total: {fastest_non_legendary['Total']}")
print("\n" + "="*50 + "\n")

# 2. Create pivot table: average Total by Generation and Type 1 (top 5 types)
pivot_table = df.pivot_table(
    values='Total',
    index='Generation',
    columns='Type 1',
    aggfunc='mean'
)

# Get top 5 most common types
top_types = df['Type 1'].value_counts().head(5).index.tolist()
print("Average Total by Generation (Top 5 Types):")
print(pivot_table[top_types])
print("\n" + "="*50 + "\n")

# 3. Pokémon with most balanced stats (lowest standard deviation)
stat_columns = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed']
df['Stat_Std'] = df[stat_columns].std(axis=1)
most_balanced = df.loc[df['Stat_Std'].idxmin()]
print("Pokémon with most balanced stats:")
print(f"Name: {most_balanced['Name']}")
print(f"Standard Deviation: {most_balanced['Stat_Std']:.2f}")
print(f"Stats: {most_balanced[stat_columns].values.tolist()}")
print("\n" + "="*50 + "\n")

# 4. Identify duplicate names and extract base names
# First, let's see how many unique names we have
print(f"Total unique names: {df['Name'].nunique()}")
print(f"Total rows: {len(df)}")

# Extract base names by removing prefixes
def extract_base_name(name):
    # Remove Mega, Primal, and forme indicators
    for prefix in ['Mega ', 'Primal ', 'Altered ', 'Origin ', 'Normal ', 'Attack ',
                   'Defense ', 'Speed ', 'Therian ', 'Incarnate ', 'Zen ', 'Blade ',
                   'Shield ', 'Confined', 'Unbound', 'Land ', 'Sky ']:
        name = name.replace(prefix, '')
    
    # Remove forme suffixes
    for suffix in [' Forme', ' Mode', ' Size', ' Rotom', ' Kyurem']:
        name = name.replace(suffix, '')
    
    return name.strip()

df['Base_Name'] = df['Name'].apply(extract_base_name)
base_name_counts = df['Base_Name'].value_counts()
duplicate_names = base_name_counts[base_name_counts > 1]
print(f"\nPokémon with multiple forms (appear more than once): {len(duplicate_names)}")
print("\nTop 10 Pokémon with most forms:")
print(duplicate_names.head(10))
print("\n" + "="*50 + "\n")

# 5. Rank all Pokémon by Total
df['Rank'] = df['Total'].rank(method='min', ascending=False).astype(int)
print("Top 10 Pokémon by Total:")
print(df[['Rank', 'Name', 'Total', 'Type 1', 'Type 2']].sort_values('Rank').head(10))

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(15, 10))

# 1. Bar chart of top 10 most common Type 1
plt.subplot(2, 2, 1)
top_10_types = df['Type 1'].value_counts().head(10)
top_10_types.plot(kind='bar', color='skyblue')
plt.title('Top 10 Most Common Primary Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.xticks(rotation=45)

# 2. Histogram of Total stat
plt.subplot(2, 2, 2)
df['Total'].hist(bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Total Stats')
plt.xlabel('Total')
plt.ylabel('Frequency')

# 3. Scatter plot: Attack vs Defense, colored by Legendary
plt.subplot(2, 2, 3)
legendary_colors = {True: 'gold', False: 'steelblue'}
colors = df['Legendary'].map(legendary_colors)
plt.scatter(df['Attack'], df['Defense'], c=colors, alpha=0.6, s=50)
plt.title('Attack vs Defense (Gold = Legendary)')
plt.xlabel('Attack')
plt.ylabel('Defense')

# Add a reference line for balanced stats
max_stat = max(df['Attack'].max(), df['Defense'].max())
plt.plot([0, max_stat], [0, max_stat], 'r--', alpha=0.3, label='Balanced')
plt.legend()

# 4. Boxplot of Total by Generation
plt.subplot(2, 2, 4)
df.boxplot(column='Total', by='Generation', grid=False)
plt.title('Total Stats Distribution by Generation')
plt.suptitle('')
plt.xlabel('Generation')
plt.ylabel('Total')

plt.tight_layout()
plt.show()

# Additional visualization: Correlation heatmap
plt.figure(figsize=(10, 8))
numeric_cols = ['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed', 'Total']
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Stat Correlation Matrix')
plt.show()
def pokemon_analyzer(df, search_name):
    """
    Analyzes a Pokémon and provides detailed information.
    
    Parameters:
    df (DataFrame): Pokémon dataset
    search_name (str): Name or partial name of Pokémon to search
    
    Returns:
    dict: Dictionary containing analysis results
    """
    
    # Case-insensitive search
    mask = df['Name'].str.lower().str.contains(search_name.lower(), na=False)
    results = df[mask]
    
    if len(results) == 0:
        return {
            'found': False,
            'message': f"No Pokémon found with name containing '{search_name}'"
        }
    
    # Get the first match (you could modify to show all matches)
    pokemon = results.iloc[0]
    
    # Calculate some advanced stats
    offensive_power = pokemon['Attack'] + pokemon['Sp. Atk'] + pokemon['Speed']
    defensive_power = pokemon['HP'] + pokemon['Defense'] + pokemon['Sp. Def']
    balance_ratio = min(offensive_power, defensive_power) / max(offensive_power, defensive_power)
    
    # Determine role based on stats
    if pokemon['Attack'] > pokemon['Sp. Atk'] and pokemon['Attack'] > pokemon['Defense']:
        role = "Physical Attacker"
    elif pokemon['Sp. Atk'] > pokemon['Attack'] and pokemon['Sp. Atk'] > pokemon['Defense']:
        role = "Special Attacker"
    elif pokemon['Defense'] > pokemon['Attack'] and pokemon['Defense'] > pokemon['Sp. Atk']:
        role = "Defensive Wall"
    else:
        role = "Mixed/Utility"
    
    # Get similar Pokémon (same Type 1 and similar Total)
    similar_mask = (df['Type 1'] == pokemon['Type 1']) & \
                   (df['Total'].between(pokemon['Total'] - 50, pokemon['Total'] + 50)) & \
                   (df['Name'] != pokemon['Name'])
    similar = df[similar_mask].head(3)
    
    # Build analysis dictionary
    analysis = {
        'found': True,
        'name': pokemon['Name'],
        'id': int(pokemon['ID']),
        'type1': pokemon['Type 1'],
        'type2': pokemon['Type 2'] if pd.notna(pokemon['Type 2']) and pokemon['Type 2'] != 'None' else None,
        'generation': int(pokemon['Generation']),
        'legendary': bool(pokemon['Legendary']),
        'total': int(pokemon['Total']),
        'stats': {
            'HP': int(pokemon['HP']),
            'Attack': int(pokemon['Attack']),
            'Defense': int(pokemon['Defense']),
            'Sp. Atk': int(pokemon['Sp. Atk']),
            'Sp. Def': int(pokemon['Sp. Def']),
            'Speed': int(pokemon['Speed'])
        },
        'analysis': {
            'role': role,
            'offensive_power': offensive_power,
            'defensive_power': defensive_power,
            'balance_ratio': round(balance_ratio, 2),
            'balanced': balance_ratio > 0.8,
            'power_level': 'High' if pokemon['Total'] > 550 else 'Medium' if pokemon['Total'] > 450 else 'Low'
        },
        'similar_pokemon': similar[['Name', 'Type 1', 'Type 2', 'Total']].to_dict('records') if len(similar) > 0 else None,
        'all_matches': results['Name'].tolist() if len(results) > 1 else None
    }
    
    return analysis

def print_pokemon_analysis(analysis):
    """Pretty print the analysis results."""
    
    if not analysis['found']:
        print(analysis['message'])
        return
    
    print("="*50)
    print(f"POKÉMON ANALYSIS: {analysis['name']}")
    print("="*50)
    
    # Basic info
    print(f"\n📊 BASIC INFO")
    print(f"  ID: #{analysis['id']:03d}")
    print(f"  Types: {analysis['type1']}" + (f"/{analysis['type2']}" if analysis['type2'] else ""))
    print(f"  Generation: {analysis['generation']}")
    print(f"  Legendary: {'⭐ YES' if analysis['legendary'] else 'No'}")
    print(f"  Total Stats: {analysis['total']}")
    
    # Stats
    print(f"\n⚔️  STATS")
    stats = analysis['stats']
    for stat, value in stats.items():
        # Create a simple bar visualization
        bar_length = int(value / 255 * 20)
        bar = '█' * bar_length + '░' * (20 - bar_length)
        print(f"  {stat:8s}: {value:3d} {bar}")
    
    # Analysis
    print(f"\n📈 ANALYSIS")
    analysis_data = analysis['analysis']
    print(f"  Role: {analysis_data['role']}")
    print(f"  Power Level: {analysis_data['power_level']}")
    print(f"  Offensive Power: {analysis_data['offensive_power']}")
    print(f"  Defensive Power: {analysis_data['defensive_power']}")
    print(f"  Balanced: {'✓ Yes' if analysis_data['balanced'] else '✗ No'} (Ratio: {analysis_data['balance_ratio']})")
    
    # Similar Pokémon
    if analysis['similar_pokemon']:
        print(f"\n🔍 SIMILAR POKÉMON")
        for similar in analysis['similar_pokemon']:
            print(f"  • {similar['Name']} ({similar['Type 1']}" + 
                  (f"/{similar['Type 2']}" if similar['Type 2'] != 'None' else "") + 
                  f") - Total: {similar['Total']}")
    
    # Multiple matches
    if analysis['all_matches'] and len(analysis['all_matches']) > 1:
        print(f"\n🔎 MULTIPLE MATCHES FOUND:")
        for match in analysis['all_matches']:
            if match != analysis['name']:
                print(f"  • {match}")

# Example usage
print("\n" + "="*50)
print("POKÉMON ANALYZER DEMO")
print("="*50)

# Test cases
test_pokemon = ["Pikachu", "Charizard", "Mewtwo", "blaziken", "gyarados", "xyz123"]

for pokemon_name in test_pokemon:
    print(f"\n\nSearching for: '{pokemon_name}'")
    print("-"*30)
    result = pokemon_analyzer(df, pokemon_name)
    print_pokemon_analysis(result)

print("\n" + "="*50)
print("ANALYSIS COMPLETE!")
print("="*50)