
import numpy as np
import pandas as pd


df = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["A", "B"])
print(df)

# What Axis Really Means

"""
df.shape
(# of Rows, # of Columns)
(axis 0, axis 1)
source: https://www.youtube.com/watch?v=PtO3t6ynH-8
"""

df.drop('B', axis=1)
print(df)

df.drop(2, axis=0)
print(df)

# Pivot tables
"""
Last but certainly not least is pivot tables. If you’re familiar with Microsoft Excel, 
then you’ve probably heard of pivot tables in some respect. 
The Pandas built-in pivot_table function creates a spreadsheet-style pivot table as a DataFrame. 
Note that the levels in the pivot table are stored in MultiIndex objects on the index and columns 
of the resulting DataFrame.

Source: https://www.youtube.com/watch?time_continue=105&v=xPPs59pn6qU
"""