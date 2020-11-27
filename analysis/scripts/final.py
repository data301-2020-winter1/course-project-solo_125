import determine_winner_by_county
import pandas as pd
df = determine_winner_by_county.func()
data = {'year':[2000,2004,2008,2012,2016],"Winner":[False,False,True,True,False]}
df_wins = pd.DataFrame(data)
df = df.merge(df_wins,on='year')
df["cor_pred"] = (df["win"] == df["Winner"])
df["cor_pred"] = df["cor_pred"].astype("int32")
df = df.groupby(["state_po","county"])["cor_pred"].sum().reset_index().sort_values(by='cor_pred',ascending=False).reset_index(drop=True)
df_final = df.loc[df['cor_pred']==5]
df_final.to_csv("final_results.csv")
