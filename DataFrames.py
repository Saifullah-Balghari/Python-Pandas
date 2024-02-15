import pandas as pd
import numpy as np
import os
# NumPy array as Pandas DataFrame
print(pd.DataFrame(np.random.randint(100, size=(5, 5))))
# OutPut:
    #     0   1   2   3   4
    # 0  38   9  16  13  36
    # 1  11  42  68  59  15
    # 2  42  28  52  82  24
    # 3   7  71  63  93  75
    # 4  91  78  65  33  34

# Python Dictionary as Pandas DataFrame.
my_dict = { "Subjects": ["Mathematics", "Computer", "Physics", "English", "Urdu", "Islamiyat"],
            "Marks" : ["78", "100", "86", "89", "92", "85"],
            "Total Marks" : ["100", "100", "100", "100", "100", "100"]
          }
print(pd.DataFrame(my_dict))
# OutPut:
    #     Subjects Marks Total Marks
    # 0  Mathematics    78         100
    # 1     Computer   100         100
    # 2      Physics    86         100
    # 3      English    89         100
    # 4         Urdu    92         100
    # 5    Islamiyat    85         100


# CSV as Pandas DataFrame
path = os.path.join("Data", "SampleCSV10rows.csv")
print(pd.read_csv(path, encoding='latin1'))
# OutPut:
    #     1   Eldon Base for stackable storage shelf, platinum Muhammed MacIntyre    3  -213.25   38.94     35  Nunavut          Storage & Organization   0.8
    # 0   2  1.7 Cubic Foot Compact "Cube" Office Refrigera...       Barry French  293   457.81  208.16  68.02  Nunavut                      Appliances  0.58
    # 1   3   Cardinal Slant-D® Ring Binder, Heavy Gauge Vinyl       Barry French  293    46.71    8.69   2.99  Nunavut  Binders and Binder Accessories  0.39
    # 2   4                                               R380      Clay Rozendal  483  1198.97  195.99   3.99  Nunavut    Telephones and Communication  0.58
    # 3   5                           Holmes HEPA Air Purifier     Carlos Soltero  515    30.94   21.78   5.94  Nunavut                      Appliances  0.50
    # 4   6  G.E. Longer-Life Indoor Recessed Floodlight Bulbs     Carlos Soltero  515     4.43    6.64   4.95  Nunavut              Office Furnishings  0.37
    # 5   7  Angle-D Binders with Locking Rings, Label Holders       Carl Jackson  613   -54.04    7.30   7.72  Nunavut  Binders and Binder Accessories  0.38
    # 6   8            SAFCO Mobile Desk Side File, Wire Frame       Carl Jackson  613   127.70   42.76   6.22  Nunavut          Storage & Organization   NaN
    # 7   9              SAFCO Commercial Wire Shelving, Black     Monica Federle  643  -695.26  138.14  35.00  Nunavut          Storage & Organization   NaN
    # 8  10                                          Xerox 198    Dorothy Badders  678  -226.36    4.98   8.33  Nunavut                           Paper  0.38