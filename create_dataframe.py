import pandas as pd
def create_dataframe(pal, df):
    pal_df = df[df[df.keys()] == pal].dropna(how="all").dropna(how="all", axis=1)
    return pal_df