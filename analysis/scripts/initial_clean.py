import pandas as pd


def load_prep(url):
    idf = (
        pd.read_csv(url)
    )
    df = (
        idf
            .drop(idf[idf["party"] == "green"].index)
            .dropna()
            .drop(columns=["version", "FIPS", "state", "office"])
    )
    return df


print(load_prep(
    "/Users/gor154/Documents/Workspaces.nosync/COSC 301 Git/course-project-solo_125/data/raw/countypres_2000-2016.csv"))
