import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
data_path = Path('data') / 'pokemon.csv'
df = pd.read_csv(data_path)

# Display the first few rows of the dataframe
print(df.head())

# Rows and Columns
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")

# Column Names
print("Column names:", df.columns.tolist())

# Data Types
print("Data types:\n", df.dtypes)

# Summary Statistics
print("Summary statistics:\n", df.describe())

# Finding highest total column value
max_total = df['Total'].idxmax()
print(f"Pokemon with highest total stats: {df.loc[max_total, 'Name']} with Total = {df.loc[max_total, 'Total']}")

# Finding the element at a specific index
index = 25
print(f"Element at index {index}:\n", df.iloc[index])

# Handeling missing values
print("Missing values in each column:\n", df.isnull().sum())
df.fillna(df.mean(numeric_only=True), inplace=True)
print("Data after filling missing values:")
df.isnull().sum()

# Fixing columns names
df.columns = [col.strip().replace(' ', '_').lower() for col in df.columns]
print("Fixed column names:", df.columns.tolist())

# Renaming column
df.rename(columns={'#': 'ID'}, inplace=True)

# Converting column data types
df['ID'] = df['ID'].astype(int)
print("Data types after conversion:\n", df.dtypes)

# Removing duplicates
df.drop_duplicates(inplace=True)
print(f"Number of rows after removing duplicates: {df.shape[0]}")

# Basic String Cleaning
df['name'] = df['name'].str.strip().str.title()
print("Cleaned names:\n", df['name'].head())

# Mean, Median, Mode
print("Mean of Total:", df['total'].mean())
print("Median of Total:", df['total'].median())
print("Mode of Total:", df['total'].mode()[0])

# Standard Deviation and Variance
print("Standard Deviation of Total:", df['total'].std())
print("Variance of Total:", df['total'].var())

# Minimum and Maximum
print("Minimum of Total:", df['total'].min())
print("Maximum of Total:", df['total'].max())

# Type 1 groupby and aggregation
type1_stats = df.groupby('type_1')['total'].agg(['mean', 'sum', 'count'])
print("Type 1 stats:\n", type1_stats)

# Create a 2x2 grid of subplots in one window
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Plot 1: Histogram (top-left, 0,0)
sns.histplot(x=df['total'], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title('Distribution of Total Stats')
axes[0, 0].set_xlabel('Total Stats')
axes[0, 0].set_ylabel('Frequency')

# Plot 2: Boxplot (top-right, 0,1)
sns.boxplot(x='legendary', y='attack', data=df, ax=axes[0, 1])
axes[0, 1].set_title('Attack by Legendary Status')
axes[0, 1].set_xlabel('Legendary')
axes[0, 1].set_ylabel('Attack')

# Plot 3: Bar chart (bottom-left, 1,0)
avg_total_by_type = df.groupby('type_1')['total'].mean().sort_values()
sns.barplot(x=avg_total_by_type.index, y=avg_total_by_type.values, ax=axes[1, 0])
axes[1, 0].set_title('Average Total Stats by Type 1')
axes[1, 0].set_xlabel('Type 1')
axes[1, 0].set_ylabel('Average Total Stats')
axes[1, 0].tick_params(axis='x', rotation=45)

# Plot 4: Scatter plot (bottom-right, 1,1)
sns.scatterplot(x='attack', y='defense', hue='type_1', data=df, ax=axes[1, 1])
axes[1, 1].set_title('Attack vs Defense')
axes[1, 1].set_xlabel('Attack')
axes[1, 1].set_ylabel('Defense')
axes[1, 1].legend(title='Type 1', bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout and show everything in one window
plt.tight_layout()
plt.show()

# Close the plot to free memory
plt.close(fig)
