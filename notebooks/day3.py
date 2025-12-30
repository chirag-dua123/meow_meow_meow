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