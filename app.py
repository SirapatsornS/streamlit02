import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#set to wide page
st.set_page_config(layout='wide')

st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')

#create mutiselected filter to represent to graph
owners = st.sidebar.multiselect(
    'Tree Owner Filter',
    trees_df['caretaker'].unique()
    #count distinct
)

if owners:
    trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(
    #สร้างกราฟโดย group จาก column dbh แล้วนับจำนวน tree_id (นับจำนวนต้นไม้)
    trees_df.groupby(['dbh']).count()['tree_id']
)
df_dbh_grouped.columns = ['tree_count']

#represent graph into column
col1,col2,col3 = st.columns(3)
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

#insert 1 line
st.divider()



st.caption('กราฟแสดงจำนวนต้นไม้ จัดกบุ่มตามเส้นผ่านศูนย์กลาง')
st.title('แปลผล')
st.write("""
  ส่วนใหญ่ของต้นไม้ใน sf มีเส้นผ่าศูนย์กลาง 3' (2721 ต้น)
""")

