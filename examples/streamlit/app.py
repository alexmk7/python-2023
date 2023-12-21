import streamlit as st
import pandas as pd
    
st.write("Test Streamlit App")
    
df = pd.read_csv("../../data/currencies.csv", index_col=0, header=0, parse_dates=[0])
st.line_chart(df)
st.dataframe(df)