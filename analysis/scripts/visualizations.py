import initial_clean
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = initial_clean.load_prep("/Users/gor154/Documents/Workspaces.nosync/COSC 301 Git/course-project-solo_125/data/raw/countypres_2000-2016.csv")
df['percent'] = df['candidatevotes']/df['totalvotes']*100
df2 = df[df.index % 2 == 0]
df1 = df[df.index%2 != 0]
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
df1 = df1.reset_index()
df2 = df2.reset_index()
df3 = df1.melt(id_vars=["state_po","percent"]).sort_values(by=['state_po'])
df3 = df3.drop(columns=["variable","value"])
plt.figure(figsize=(5, 9))
sns.violinplot(data=df3,x="percent",y="state_po",width=4).set_title('Republican Leaning of States')
plt.show()
df4 = df2.melt(id_vars=["state_po","percent"]).sort_values(by=['state_po'])
df4 = df4.drop(columns=["variable","value"])
plt.figure(figsize=(5, 9))
sns.violinplot(data=df4,x="percent",y="state_po",width=4).set_title('Democratic Leaning of States')
plt.show()
