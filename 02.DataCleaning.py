import pandas as pd
import os

## Data Cleaning: Fixing bad data like: Empty cells, Data in wrong format, Wrong data and Duplicates

path = os.path.join("Data", "UncleanedCSV.csv")
df = pd.read_csv(path, encoding='latin1')

# Cleaning rows that contains empty cells
df = df.dropna()

# Cleaning wrong formats
df['Date'] = df['Date'].str.replace("'", "")
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')

# Replacing values
df.loc[3, 'Duration'] = 45

# Removing Duplicates
df.drop_duplicates(inplace = True)
print(df)
df1 = df
df1.to_csv("Data//CleanedCSV.csv", index=False)