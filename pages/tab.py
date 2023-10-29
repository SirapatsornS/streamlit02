import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#set to wide page
st.set_page_config(layout='wide')

st.markdown('สวัสดี! *Streamlit*')
st.title('Tab Layout and Decoration')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')

df_dbh_grouped = pd.DataFrame(
    #สร้างกราฟโดย group จาก column dbh แล้วนับจำนวน tree_id (นับจำนวนต้นไม้)
    trees_df.groupby(['dbh']).count()['tree_id']
)
df_dbh_grouped.columns = ['tree_count']

tab1,tab2,tab3 = st.tabs(['Line Chart','Bar Chart','Area Chart'])
with tab1:
    st.line_chart(df_dbh_grouped)
with tab2:
    st.bar_chart(df_dbh_grouped)
with tab3:
    st.area_chart(df_dbh_grouped)

