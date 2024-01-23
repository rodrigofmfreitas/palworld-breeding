import pandas as pd
import numpy as np
import streamlit as st
from IPython.display import display

df = pd.read_csv("dataframe.csv", index_col=1).drop(columns=["Unnamed: 0"])

pals = list(df.keys())
pal = st.selectbox("Check Pal options", pals)
pal_df = df[df[df.keys()] == pal]
pal_df.dropna(how="all", inplace=True).dropna(how="all", axis=1, inplace=True)

pal_df