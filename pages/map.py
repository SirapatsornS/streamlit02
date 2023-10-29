import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#set to wide page
st.set_page_config(layout='wide')

st.markdown('สวัสดี! *Streamlit*')
st.title('Map of San Francisco Tree')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')

#create map tree
trees_df = trees_df.dropna(subset=['longitude','latitude'])
trees_df = trees_df.sample(n=1000,replace=True)
st.map(trees_df)