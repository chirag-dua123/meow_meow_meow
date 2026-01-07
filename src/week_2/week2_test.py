#Part A
#Task A.1
'''
### Difference between df.loc and df.iloc
**`df.loc`** is **label-based indexing**. It selects data using explicit row/column labels (e.g., index names or column names).  
- **Examples**:  
  - `df.loc['row_label']`: Selects a row by its index label.  
  - `df.loc[:, 'column_name']`: Selects a column by name.  
  - `df.loc['A':'C', ['col1', 'col2']]`: Selects rows with labels 'A' to 'C' and specific columns.  
- **Key behavior**: Slicing includes the **end label** (e.g., `'A':'C'` includes 'C').  

**`df.iloc`** is **integer-position-based indexing**. It selects data using numerical positions (0-based indexing).  
- **Examples**:  
  - `df.iloc[0]`: Selects the first row.  
  - `df.iloc[:, 1]`: Selects the second column.  
  - `df.iloc[0:3, [0, 1]]`: Selects rows 0, 1, 2 and columns 0, 1.  
- **Key behavior**: Slicing **excludes the end index** (e.g., `0:3` includes positions 0, 1, 2).  

**Why it matters**:  
- Use `loc` when working with **meaningful labels** (e.g., dates, IDs).  
- Use `iloc` for **positional access** (e.g., "first 5 rows").  
- Mixing them up causes errors (e.g., `df.iloc['A']` fails).  

---

### NaN vs None in pandas
**`NaN` (Not a Number)**:  
- A **floating-point sentinel value** from NumPy (`np.nan`).  
- Used for **missing numerical data**.  
- Behaves oddly: `NaN == NaN` evaluates to `False`.  
- Propagates in calculations (e.g., `10 + NaN = NaN`).  

**`None`**:  
- Python’s built-in **null value** (object type).  
- Used for **missing non-numerical data** (e.g., strings, objects).  

**Key differences**:  
| Aspect          | `NaN`                            | `None`                     |  
|-----------------|----------------------------------|----------------------------|  
| **Type**        | Float (`np.float64`)             | `NoneType`                 |  
| **Usage**       | Numerical columns                | Object/string columns      |  
| **Operations**  | Optimized for speed (vectorized)| Slower (Python-level)      |  
| **Check**       | `pd.isna()` or `np.isnan()`      | `is None` (but use `pd.isna()` for consistency) |  

**Practical note**:  
Pandas often converts `None` to `NaN` internally for efficiency. Always use `pd.isna()` to check for missing values uniformly.  

---

### When to use groupby().agg() instead of value_counts()
**`value_counts()`**:  
- Counts **unique values in a single column**.  
- Returns a Series: `{value: count}`.  
- **Example**: `df['color'].value_counts()` → counts red/blue/green.  

**`groupby().agg()`**:  
- **Groups by one/more columns**, then applies **custom aggregations** (e.g., mean, sum, multiple stats).  
- Handles **multiple columns** simultaneously.  
- **Example**:  
  ```python
  df.groupby('category').agg({'sales': 'sum', 'profit': 'mean'})
  ```  

**Use `groupby().agg()` when**:  
1. You need **multiple statistics** (e.g., sum + mean) per group.  
2. You’re grouping by **multiple columns** (e.g., `groupby(['city', 'product'])`).  
3. You need **non-count aggregations** (e.g., average, max).  
4. You require **custom functions** (e.g., `lambda x: x.std() / x.mean()`).  

**Use `value_counts()` for**:  
- Quick frequency counts of a **single categorical column**.  
- Normalized counts (e.g., `normalize=True`).  

---

### Mean vs median — when is median better?
**Mean**: Sum of values divided by count. Sensitive to **outliers and skew**.  
**Median**: Middle value in a sorted list. **Robust to outliers**.  

**Median is better when**:  
1. **Outliers exist**:  
   - Salary data: One billionaire skews the mean, but median reflects "typical" salary.  
2. **Skewed distributions**:  
   - Log-normal data (e.g., house prices, income): Median avoids distortion from the tail.  
3. **Ordinal data**:  
   - Survey responses (e.g., "1=poor, 5=excellent"): Median is more intuitive.  

**Mean is better when**:  
- Data is **symmetric and outlier-free** (e.g., heights of adults).  
- You need **mathematical properties** (e.g., sum of residuals = 0 in linear regression).  

**Rule of thumb**: Plot a histogram. If skewed or with outliers, use median.  

---

### What does axis=0 vs axis=1 mean?
- **`axis=0`**: **Rows** (vertical direction). Operations **collapse columns**.  
  - Example: `df.sum(axis=0)` → Sums **each column** (result has 1 row per column).  
- **`axis=1`**: **Columns** (horizontal direction). Operations **collapse rows**.  
  - Example: `df.sum(axis=1)` → Sums **each row** (result has 1 column per row).  

**Memory aid**:  
- `axis=0` = "down" the rows (column-wise).  
- `axis=1` = "across" the columns (row-wise).  

**Critical in functions like**:  
- `dropna(axis=0)`: Drop rows with missing values.  
- `apply(func, axis=1)`: Apply `func` to each row.  

---

### Difference between apply, map, and vectorized ops
**Vectorized operations**:  
- **Fastest**. Operations applied to **entire arrays** at once (C-optimized).  
- **Example**: `df['col'] * 2`, `np.log(df['col'])`.  
- **Use when**: Simple math/transformations on homogeneous data.  

**`map`**:  
- **Series-only**. Applies a function/mapping **element-wise** to a Series.  
- Accepts dicts, Series, or functions.  
- **Example**: `df['col'].map({'A': 1, 'B': 2})` or `df['col'].map(lambda x: x*2)`.  
- **Faster than `apply` for element-wise ops** but less flexible.  

**`apply`**:  
- **Flexible but slowest**. Applies a function **along an axis** (rows/columns) of a DataFrame or element-wise to a Series.  
- **DataFrame example**: `df.apply(lambda row: row['A'] + row['B'], axis=1)` (row-wise).  
- **Series example**: `df['col'].apply(str.lower)`.  
- **Use when**: Complex logic that can’t be vectorized (e.g., custom row-wise conditions).  

**Performance hierarchy**:  
Vectorized > `map` (for Series) > `apply` (avoid if possible).  

---

### What is EDA and why do we do it before modeling?
**EDA (Exploratory Data Analysis)**:  
Process of **summarizing, visualizing, and interrogating data** to uncover patterns, anomalies, relationships, and insights before modeling.  

**Key techniques**:  
- Summary stats (`df.describe()`).  
- Visualizations (histograms, box plots, scatter plots).  
- Handling missing values/outliers.  
- Correlation analysis.  
- Feature distribution checks.  

**Why do EDA before modeling?**  
1. **Understand data structure**: Identify data types, missing values, and potential errors.  
2. **Detect biases/issues**:  
   - Class imbalance (e.g., 95% "no" in fraud detection).  
   - Outliers distorting relationships.  
   - Leakage (e.g., future data in features).  
3. **Feature engineering**:  
   - Create new features (e.g., extract month from date).  
   - Transform skewed features (e.g., log transform).  
4. **Validate assumptions**:  
   - Linear models assume linearity/homoscedasticity—EDA checks this.  
5. **Guide modeling choices**:  
   - Tree-based models handle outliers better; linear models need scaling.  
6. **Avoid garbage-in-garbage-out**: Fixing data issues early prevents wasted effort on flawed models.  

**Without EDA**: Models may fail silently (e.g., poor generalization due to undetected leakage). EDA builds intuition and trust in results.  

---  
*Answers reflect best practices as of 2026. Tools like Polars are gaining traction, but pandas fundamentals remain essential.*
'''

#Task A.2

import pandas as pd
from pathlib import Path

path = Path('data') / 'pokemon.csv'
df = pd.read_csv(path)

avg_hp = df["HP"].mean
fire = df[df["Type 1"] == 'Fire']
print(avg_hp)
print(fire.shape)

#Task 3
'''
Since mean is greater than median we can conclude that there are some very high attack pokemons that are increasing the attach mean disproportionately high in comparision to others. From out domain knowledge we can also conclude that some fighting type and dragon type pokemons are having very high attack score in comparision to others.
'''

#Part B
#Task B.1
print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.describe())
'''
From the results of df.dtypes we can conclude that all columns are numeric type except Name, Type 1, Type 2 and Legendary columns which are of object type. Catagorical columns are Type 1, Type 2 and Legendary. Name column is unique for each pokemon so it cannot be treated as categorical column.
'''
import numpy as np
#Task B.2
df.isnull().sum()
df['Type 2'].fillna('Unknown', inplace=True)
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
print(df)

#fixing column names to snake case
df.columns = [col.lower().replace(' ', '_') for col in df.columns]
print(df.columns)

#converting type 1 and type 2 columns to lower case
df['type_1'] = df['type_1'].str.lower()
df['type_2'] = df['type_2'].str.lower()

#remove duplicates
df.drop_duplicates(inplace=True)
print(df.shape)

#Task B.3
import matplotlib.pyplot as plt
import seaborn as sns
