import pandas as pd
import streamlit as st

from create_dataframe import create_dataframe

df = pd.read_csv("dataframe.csv", index_col=1).drop(columns=["Unnamed: 0"])

pals = list(df.keys())
pal = st.selectbox("Check Pal options", pals)

pal_df = create_dataframe(pal, df)

pal_df