import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Documents")
   st.text_area("Test1","","Model Sexual Harassment Policy.pdf")

with col2:
   st.header("Topics")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Content")
