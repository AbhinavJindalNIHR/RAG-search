import streamlit as st
import pandas as pd
from dataimport import df

st.set_page_config(page_title="NIHR Awards Data", page_icon="📈")

st.markdown("# NIHR Awards Data")
st.sidebar.header("NIHR Awards Data")
st.write(
    """You can view NIHR Awards dataset here - which provides a list of NIHR supported research across the UK.!"""
)
container = st.container()
for i in range(0, len(df), 50):
    container.dataframe(df[i:i+50])