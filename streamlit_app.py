import pandas as pd
import streamlit as st

from create_dataframe import create_dataframe

df = pd.read_csv("dataframe.csv", index_col=1).drop(columns=["Unnamed: 0"])

pals = list(df.keys())
pal = st.selectbox("Check Pal options", pals)

df1 = df[df[df.keys()] == pal].dropna(how="all").dropna(how="all", axis=1)
pal_dict = df1.to_dict()

pal_tuples = []
for i in pal_dict:
    for j in pal_dict[i]:
        if pal_dict[i][j] == "Suzaku":
            pal_tuples.append((i, j))
res = list({*map(tuple, map(sorted, pal_tuples))})
df = pd.DataFrame(res, columns=["Parent 1", "Parent 2"])

df