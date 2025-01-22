"""
    This python script is related to the Eda part of our Streamlit Web App.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# this is how we import streamlit
import streamlit as st
st.title('Penguins day')
st.image('penguins.png', caption='I love Quack')
st.header('this creates a paragraph')
st.write("Let's show some data about penguins")
st.markdown("Where is the data?")

df = pd.read_csv('./data/penguins_geo.csv')
print(df.dtypes)

st.dataframe(df['bill_length_mm'])





