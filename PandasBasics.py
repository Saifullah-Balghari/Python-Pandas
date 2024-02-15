import pandas as pd
import os

# my_dict = { "Subjects": ["Mathematics", "Computer", "Physics", "English", "Urdu", "Islamiyat"],
#             "Marks" : ["78", "100", "86", "89", "92", "85"],
#             "Total Marks" : ["100", "100", "100", "100", "100", "100"]
#           }

# dataframe = pd.DataFrame(my_dict)
# print(dataframe)
path = os.path.join("Data", "SampleCSV10000rows.csv")
df = pd.read_csv(path, encoding='latin1')
print(df)