# Week2_Pokemon_DataAnalysis.py
# (This script demonstrates data loading, cleaning, EDA, and visualization on Pokemon data)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Data Loading and Inspection
# Read the CSV file into a DataFrame using a path relative to the repository root
data_path = Path(__file__).resolve().parents[3] / 'data' / 'pokemon.csv'
df = pd.read_csv(data_path)

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
# First, normalize column names so downstream code can rely on consistent names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(r"\W+", "_", regex=True)
    .str.strip("_")
)

# For numeric columns, fill NaNs with column mean; for categorical, use mode
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_cols:
    mean_val = df[col].mean()
    df[col] = df[col].fillna(mean_val)
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    mode_val = df[col].mode()[0] if not df[col].mode().empty else ''
    df[col] = df[col].fillna(mode_val)

print(df.isnull().sum())  # Confirm no missing values remain after fill
# Q: What might be the advantage of filling missing data with mean/mode instead of dropping?
print(df.dtypes)  # View current data types


# Convert certain columns if needed (guarding for missing columns)
if 'capture_rate' in df.columns and df['capture_rate'].dtype == object:
    df['capture_rate'] = pd.to_numeric(df['capture_rate'], errors='coerce')

# Normalize legendary flag: many datasets use 'legendary' column
if 'is_legendary' not in df.columns and 'legendary' in df.columns:
    df['is_legendary'] = df['legendary'].astype(bool)
elif 'is_legendary' in df.columns:
    df['is_legendary'] = df['is_legendary'].astype(bool)

print(df.dtypes)  # Re-check types
# Q: After conversion, did any NaNs appear when casting? How to handle unexpected types?
# show cleaned columns
print(df.columns.tolist())

# Remove duplicate rows, if any
df = df.drop_duplicates()
print(df.shape)  # New shape after dropping duplicates
# Q: Why might duplicate records be present, and how does drop_duplicates() decide which to keep?
# Example 1: Total base stats (sum whichever stat columns exist)
stat_candidates = ['hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'sp_attack', 'sp_defense', 'speed']
stat_cols = [c for c in stat_candidates if c in df.columns]
if stat_cols:
    df['total_stats'] = df[stat_cols].sum(axis=1)
else:
    df['total_stats'] = pd.NA

# Example 2: Body mass index (roughly weight_kg divided by height_m^2) if available
if 'weight_kg' in df.columns and 'height_m' in df.columns:
    df['bmi'] = df['weight_kg'] / (df['height_m'] ** 2)
else:
    df['bmi'] = pd.NA
print(df[['name', 'total_stats', 'bmi']].head())

# Q: How do these new features help analysis? For instance, does higher 'total_stats' correlate with legend status?
# Summary statistics for numeric columns
print(df.describe())  # count, mean, std, min, quartiles, max:contentReference[oaicite:12]{index=12}

# Distribution of categorical variable (example: primary type)
type1 = 'type_1' if 'type_1' in df.columns else ('type1' if 'type1' in df.columns else None)
type2 = 'type_2' if 'type_2' in df.columns else ('type2' if 'type2' in df.columns else None)
if type1:
    print(df[type1].value_counts())
if type2:
    print(df[type2].value_counts())

# Correlation matrix of numeric features
print(df.select_dtypes(include=['number']).corr())  # Pairwise correlation of numeric columns
# Q: Which two stats have the strongest positive correlation? (Check the correlation matrix)
print("Mean stats:\n", df.mean(numeric_only=True))       # Column means
print("Median stats:\n", df.median(numeric_only=True))   # Column medians
print("Std dev:\n", df.std(numeric_only=True))          # Standard deviations
# Use guards for legend calculations
if 'is_legendary' in df.columns:
    print("Legendaries average total:", df[df['is_legendary']]['total_stats'].mean())
    print("Non-legend total:", df[~df['is_legendary']]['total_stats'].mean())
# Q: Compare the above two lines: do legendary Pokemon have a higher average 'total_stats' than non-legendary?
# Histogram of Attack stat
plt.figure(figsize=(6,4))
if 'attack' in df.columns:
    sns.histplot(df['attack'], bins=15, kde=True, color='skyblue')
else:
    print("Column 'attack' not found; skipping attack histogram")
plt.title('Attack Distribution')
plt.xlabel('Attack')
plt.ylabel('Count')
plt.show()  # Histograms show how data are distributed:contentReference[oaicite:19]{index=19}

# Bar plot of Pokemon primary type counts
plt.figure(figsize=(6,4))
if type1:
    sns.countplot(y=type1, data=df, order=df[type1].value_counts().index, palette='viridis')
else:
    print("No type1 column found; skipping type countplot")
plt.title('Count by Primary Type')
plt.xlabel('Count')
plt.ylabel('Type')
plt.show()  # Bar chart of categorical counts

# Box plot of Defense by Generation
plt.figure(figsize=(6,4))
if 'generation' in df.columns and 'defense' in df.columns:
    sns.boxplot(x='generation', y='defense', data=df)
else:
    print("Missing 'generation' or 'defense'; skipping boxplot")
plt.title('Defense by Generation')
plt.xlabel('Generation')
plt.ylabel('Defense')
plt.show()  # Boxplot shows quartiles and outliers:contentReference[oaicite:20]{index=20}

# Scatter plot of Attack vs. Defense
plt.figure(figsize=(6,5))
if 'attack' in df.columns and 'defense' in df.columns:
    hue_col = 'is_legendary' if 'is_legendary' in df.columns else None
    sns.scatterplot(x='attack', y='defense', hue=hue_col, data=df)
else:
    print("Missing 'attack' or 'defense'; skipping scatterplot")
plt.title('Attack vs Defense by Legendary Status')
plt.xlabel('Attack')
plt.ylabel('Defense')
plt.show()  # Scatterplot shows joint distribution of two variables:contentReference[oaicite:21]{index=21}
# Q: From the scatter plot, do legendary Pokemon (one color) tend to have higher attack/defense?
