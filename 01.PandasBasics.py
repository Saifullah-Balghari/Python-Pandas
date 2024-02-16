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


# Python Dictionary as Pandas DataFrame.
my_dict = { "Subjects": ["Mathematics", "Computer", "Physics", "Urdu"],
            "Obt_Marks" : ["78", "100", "86", "89"],
            "Total_Marks" : ["100", "100", "100", "100"]
          }
df1 = pd.DataFrame(my_dict)
print(df1)
# OutPut:
    #         Subjects   Obt_Marks  Total_Marks
    # 0  Mathematics         78          100
    # 1     Computer        100          100
    # 2      Physics         86          100
    # 3         Urdu         89          100


# CSV as Pandas DataFrame
path = os.path.join("Data", "SampleCSV.csv")
df2 = pd.read_csv(path, encoding='latin1')
print(df2)
# OutPut:
    #     Subjects   Obt_Marks  Total_Marks
    # 0  Mathematics         78          100
    # 1     Computer        100          100
    # 2      Physics         86          100
    # 3         Urdu         89          100

# XLSX as Pandas DataFrame
path = os.path.join("Data", "SampleXLSX.csv")
df3 = pd.read_excel(path, sheet_name="sheet1", encoding='latin1')
print(df3)