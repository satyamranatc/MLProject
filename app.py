import streamlit as st
import pandas as pd




Df = pd.DataFrame({
    'first_column': [1, 2, 3, 4],
    'second_column': [10, 20, 30, 40]
}) 

st.write("# Here's our first attempt at using data to create a table: ")


