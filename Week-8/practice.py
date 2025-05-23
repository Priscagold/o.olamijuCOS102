import pandas as pd

df = pd.read_csv("cryptocurrency.csv")  # replace with your filename
print(f"Number of columns: {len(df.columns)}")
print("Column names:", df.columns.tolist())
print(f"Number of rows: {len(df.rows)}")