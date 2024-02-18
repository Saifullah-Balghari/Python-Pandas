import pandas as pd
import numpy as np
import os

# Pandas Series
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s1 = pd.Series(list)
print(s1)
# Output:
    # 0    1
    # 1    2
    # 2    3
    # 3    4
    # 4    5
    # 5    6
    # 6    7
    # 7    8
    # 8    9


# Adjusting the number of ROWS to Show

# To see the default number:
print(pd.options.display.max_rows)          # Default is 60 : if contains more then 60 it will show only the first and last 10 rows

# Set the number of ROWS to Show
pd.options.display.max_rows = 99999


# Python Dictionary as Pandas DataFrame.
my_dict = { "Subjects": ["Mathematics", "Computer", "Physics", "Urdu"],
            "Obt_Marks" : ["78", "100", "86", "89"],
            "Total_Marks" : ["100", "100", "100", "100"]
          }
df = pd.DataFrame(my_dict)
print(df)
# OutPut:
    #         Subjects   Obt_Marks  Total_Marks
    # 0  Mathematics         78          100
    # 1     Computer        100          100
    # 2      Physics         86          100
    # 3         Urdu         89          100


## Reading CSV, XLSX & JSON

# CSV as Pandas DataFrame
path = os.path.join("Data", "SampleCSV.csv")
df = pd.read_csv(path, encoding='latin1')
print(df)

# XLSX as Pandas DataFrame
path = os.path.join("Data", "SampleXLSX.xlsx")
df = pd.read_excel(path, sheet_name=None)
print(df)

# JSON as Pandas DataFrame
path = os.path.join("Data", "SampleJSON.json")
df = pd.read_json(path, encoding='latin1')
print(df)

## Viewing the Data
path = os.path.join("Data", "SampleCSV.csv")
df = pd.read_csv(path, encoding='latin1')

# Viewing the head
print(df.head())        # Default is 5
print(df.head(10))      # prints the first 10 rows

# Viewing the tail
print(df.tail())        # Default is 5
print(df.tail(10))      # prints the last 10 rows

# Info About the Data
print(df.info())
# Output:
    # <class 'pandas.core.frame.DataFrame'>
    # RangeIndex: 4 entries, 0 to 3
    # Data columns (total 3 columns):
    #  #   Column       Non-Null Count  Dtype
    # ---  ------       --------------  -----
    #  0   Subjects     4 non-null      object
    #  1   Obt_Marks    4 non-null      int64
    #  2   Total_Marks  4 non-null      int64
    # dtypes: int64(2), object(1)
    # memory usage: 228.0+ bytes
    # None

## Writing DataFrames to CSV & XLSX
os.chdir("Data//")
df = pd.DataFrame({ "Subjects": ["Mathematics", "Computer", "Physics", "Urdu"],
                    "Obt_Marks" : ["78", "100", "86", "89"],
                    "Total_Marks" : ["100", "100", "100", "100"]
                })
df.to_csv("OutPutSampleCSV.csv", index=False)           # To CSV
df.to_excel("OutPutSampleXLSX.xlsx", index=False)       # To XLSX