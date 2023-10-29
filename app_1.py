import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.markdown('สวัสดี! *Streamlit*')
st.title('Layout and Decoration')
st.write("""
  เราจะลองทำ San Francisco Dataset กันดู
""")

trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(
    #สร้างกราฟโดย group จาก column dbh แล้วนับจำนวน tree_id (นับจำนวนต้นไม้)
    trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.colunms = ['tree_count']

col1,col2,col3 = st.columns(3)
with col1:
    st.line_chart(df_dbh_grouped)
with col2:
    st.bar_chart(df_dbh_grouped)
with col3:
    st.area_chart(df_dbh_grouped)

st.caption('กราฟแสดงจำนวนต้นไม้ จัดกบุ่มตามเส้นผ่านศูนย์กลาง')
st.title('แปลผล')
st.write("""
  ส่วนใหญ่ของต้นไม้ใน sf มีเส้นผ่าศูนย์กลาง 3' (2721 ต้น)
""")
