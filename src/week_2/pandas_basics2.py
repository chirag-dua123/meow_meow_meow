import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# how many rows and columns
df = pd.read_csv('titanic.csv')
# print(df.shape)

#for missing values
# print(df.isnull().sum())

#one group by result
# print(df.groupby('Pclass')['Age'].mean())

#cleaning

#fixing the column names
df.columns = df.columns.str.lower().str.replace(r'[^a-z0-9]+', '_')

#changing column types 
df['fare'] = pd.to_numeric(df['fare'], errors='coerce').round().astype('Int64')
# print(df.columns)

##Explanatory data analysis (EDA)

# Set a clean style
plt.style.use('default')  # or 'ggplot', 'bmh', etc.

# Generate sample exam scores (0–100)
np.random.seed(42)
scores = np.random.normal(loc=75, scale=15, size=200)
scores = np.clip(scores, 0, 100)  # Ensure scores stay within 0–100

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# --- Histogram ---
ax1.hist(scores, bins=15, color='steelblue', edgecolor='white', alpha=0.8)
ax1.set_title('Distribution of Exam Scores')
ax1.set_xlabel('Score')
ax1.set_ylabel('Frequency')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- Boxplot ---
ax2.boxplot(scores, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightcoral', color='black'),
            medianprops=dict(color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(marker='o', markerfacecolor='orange', markersize=4))
ax2.set_title('Spread of Exam Scores')
ax2.set_ylabel('Score')
ax2.set_xticks([1])
ax2.set_xticklabels([''])

plt.tight_layout()
plt.show()