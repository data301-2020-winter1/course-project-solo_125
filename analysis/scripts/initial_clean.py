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
            .reset_index()
    )
    return df
