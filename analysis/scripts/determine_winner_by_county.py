import initial_clean
import pandas as pd
import numpy as np

df = initial_clean.load_prep(
    "/Users/gor154/Documents/Workspaces.nosync/COSC 301 Git/course-project-solo_125/data/raw/countypres_2000-2016.csv")
df['percent'] = df['candidatevotes'] / df['totalvotes'] * 100
df2 = df[df.index % 2 == 0]
df1 = df[df.index % 2 != 0]
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
df1 = df1.reset_index()
df2 = df2.reset_index()
df3 = pd.concat([df1['percent'], df2['percent']], axis=1, keys=["Rep_per", "Dem_per"])
# A win will be defined by the Democrat winning for simplicity's sake
df3['win'] = df3['Dem_per'] > df3['Rep_per']
df2['win'] = df3['win']


def func():
    return df2
