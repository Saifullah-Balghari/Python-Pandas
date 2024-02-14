import pandas as pd

my_dict = { "Subjects": ["Mathematics", "Computer", "Physics", "English", "Urdu", "Islamiyat"],
            "Marks" : ["78", "100", "86", "89", "92", "85"],
            "Total Marks" : ["100", "100", "100", "100", "100", "100"]
          }

dataframe = pd.DataFrame(my_dict)
print(dataframe)
