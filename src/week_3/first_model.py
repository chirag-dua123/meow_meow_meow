import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from pathlib import Path

path = Path('data') / 'pokemon.csv'
df = pd.read_csv(path)   # use any clean dataset

# Select only numeric columns for features
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
if 'Total' in numeric_cols:
    numeric_cols.remove('Total')

X = df[numeric_cols]
y = df["Total"]
print("Features:", X.columns.tolist())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print("R² Score:", r2_score(y_test, preds))
print("MSE:", mean_squared_error(y_test, preds))
print("RMSE:", mean_squared_error(y_test, preds) ** 0.5)
