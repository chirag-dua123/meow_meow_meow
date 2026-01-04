# This project focuses on "What makes a pokemon strong?"
# So we will 
# 1. Load the dataset
# 2. Clean the data
# 3. Perform EDA to find insights about strong pokemon
# 4. Visualize the findings
# 5. Verify findings with correlation and statistical tests

import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def main():
    # Load the dataset
    data_path = Path('data') / 'pokemon.csv'
    df = pd.read_csv(data_path)

    # Data Cleaning
    # Fixing column names
    df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]

    # Renaming column
    df.rename(columns={'#': 'id'}, inplace=True)

    # Converting column data types
    df['id'] = pd.to_numeric(df['id'], errors='coerce')

    # Removing duplicates
    df.drop_duplicates(inplace=True)
    
    # Handling missing values
    df.fillna({'type_2': np.nan}, inplace=True)

    # Basic String Cleaning
    df['name'] = df['name'].str.strip().str.title()

    # Display cleaned data info
    print("Cleaned Data Info:")
    print(df.info())

    # Display first few rows of cleaned data
    print("First few rows of cleaned data:")
    print(df.head())
    
    # Creating a new df with mean of total for each type_1
    type_strength = df.groupby('type_1')['total'].mean().reset_index().sort_values(by='total', ascending=False)
    
    # Creating a line plot of average(mean) of total by type_1 vs type_1
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=type_strength, x='type_1', y='total', marker='o')
    plt.title('Average Total Strength by Pokemon Type')
    plt.xlabel('Pokemon Type')
    plt.ylabel('Average Total Strength')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # By the graph we can conclude that Dragon type pokemons are the strongest while bug are the weakest on average.
    
    # Now we are plotting a line plot to visualize the distribution of total strength across different generation
    generation_strength = df.groupby('generation')['total'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=generation_strength, x='generation', y='total', marker='o')
    plt.fill_between(generation_strength['generation'], generation_strength['total'], alpha=0.3)
    plt.title('Average Total Strength by Generation')
    plt.xlabel('Generation')
    plt.ylabel('Average Total Strength')
    plt.xticks(generation_strength['generation'])
    plt.tight_layout()
    plt.show()
    
    # The trends from this graph are not prominent so we won't draw any conclusions from it.
    
    # Now we will plot a area graph of total vs speed + hp + attack + defense
    plt.figure(figsize=(12, 8))
    stats = ['hp', 'attack', 'defense', 'speed']
    for stat in stats:
        sns.lineplot(data=df, x='total', y=stat, label=stat)
    plt.title('Pokemon Stats vs Total Strength')
    plt.xlabel('Total Strength')
    plt.ylabel('Stat Value')
    plt.legend()
    plt.tight_layout()
    plt.show()
    # From this graph we can conclude that from total 650 onwards the highest skill is attack followed by hp. Thus we can conclude that strong pokemons have high attack and hp stats.
    
    # Correlation Analysis
    corr = df[['total', 'hp', 'attack', 'defense', 'speed']].corr()
    print("Correlation Matrix:")
    print(corr['total'].sort_values(ascending=False))
    
    print(f'Final Conclusion: \nFrom the analysis and visualizations, we can conclude that Dragon type pokemons are the strongest on average. Additionally, strong pokemons tend to have high attack and hp stats, as indicated by both the visualizations and correlation analysis.')

if __name__ == "__main__":
    main()