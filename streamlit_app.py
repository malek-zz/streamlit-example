import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Documents")
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')
   st.text('This is some text.')

with col2:
   st.subheader("Topics")
   st.text('This is some text.')

with col3:
   st.subheader("Content")
