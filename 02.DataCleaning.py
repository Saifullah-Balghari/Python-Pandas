import pandas as pd
import os

## Data Cleaning: Fixing bad data like: Empty cells, Data in wrong format, Wrong data and Duplicates

path = os.path.join("Data", "UncleanedCSV.csv")
df = pd.read_csv(path, encoding='latin1')
print(df, "\n")

# Cleaning rows that contains empty cells
df = df.dropna()
print(df)

# Cleaning wrong formats

df = pd.read_csv(path)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce', format='%Y/%m/%d')
print(df)