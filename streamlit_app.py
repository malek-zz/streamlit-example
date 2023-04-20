import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Documents")
   st.text('This is some text.')

with col2:
   st.header("Topics")
   st.text('This is some text.')

with col3:
   st.header("Content")
