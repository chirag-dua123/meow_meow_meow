
import pandas as pd
import matplotlib.pyplot as plt

#creating the dataframe
df = pd.read_csv('titanic.csv')

#filling missing values in 'Fare' column with the mean fare
df = df.fillna(df.mean(numeric_only=True))

#making the plots
bins = 20       #number of bars (intervals)
fig, axes = plt.subplots(1, 3, figsize=(12, 4), sharey=True) #3 subplots in one row with 12x4 size that share the y axis
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']      #colors for each class
for ax, pclass, color in zip(axes, [1, 2, 3], colors):  #looping through each subplot, passenger class and color
        data = df[df['Pclass'] == pclass]['Fare'].dropna()      #getting fare data for the specific passenger class     
        ax.hist(data, bins=bins, color=color, alpha=0.75)
        ax.set_title(f'Class {pclass}')
        ax.set_xlabel('Fare')
        ax.grid(True)

axes[0].set_ylabel('Frequency')
fig.suptitle('Fare Distribution by Passenger Class')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('fare_by_pclass.png', dpi=150)

plt.show()

# Week2_Pokemon_DataAnalysis.py
# (This script demonstrates data loading, cleaning, EDA, and visualization on Pokemon data)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Data Loading and Inspection
# Read the CSV file into a DataFrame using pandas.read_csv4
df = pd.read_csv('Pokemon.csv')

# Inspect the first few rows to check the data
print(df.head())        # View top rows
print(df.shape)         # Print (rows, columns)
print(df.info())        # DataFrame info: column types and non-null counts
print(df.columns.tolist())  # List column names

# Q: Based on df.shape and df.info(), how many Pokémon and attributes are in the data?
# Q: What do we learn from df.info() about null values and data types?
# Check for missing values in each column
print(df.isnull().sum())   # Counts of NaNs per column

# Option 1: Drop rows with any missing values
df_dropna = df.dropna()
print(df_dropna.shape)     # Shape after dropping
# Q: How many rows were lost after dropna(), and which rows had missing values?

# Option 2: Fill missing values
# For numeric columns, fill NaNs with column mean; for categorical, use mode
numeric_cols = df.select_dtypes(include=['float64','int64']).columns
for col in numeric_cols:
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    mode_val = df[col].mode()[0] if not df[col].mode().empty else ''
    df[col] = df[col].fillna(mode_val)

print(df.isnull().sum())  # Confirm no missing values remain after fill
# Q: What might be the advantage of filling missing data with mean/mode instead of dropping?

