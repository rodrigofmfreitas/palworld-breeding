import pandas as pd
import streamlit as st
from IPython.display import display

df = pd.read_csv("dataframe.csv", index_col=1).drop(columns=["Unnamed: 0"])

pals = list(df.keys())
pal = st.multiselect("Check Pal options", pals)
pal_df = df[df[df.keys()] == pal].dropna(how="all").dropna(how="all", axis=1)

pal_df