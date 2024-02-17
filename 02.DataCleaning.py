import pandas as pd
import os

## Data Cleaning: Fixing bad data like: Empty cells, Data in wrong format, Wrong data and Duplicates

path = os.path.join("Data", "UncleanedCSV.csv")
df = pd.read_csv(path, encoding='latin1')
print(df, "\n")

# Removing rows that contains empty cells: dropna()
print(df.dropna(), "\n")

