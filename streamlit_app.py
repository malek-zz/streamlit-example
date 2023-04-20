import streamlit as st
from PIL import Image

image = Image.open('pdf.png')

st.image(image, caption='')
col1, col2, col3 = st.columns(3)

with col1:
   st.subheader("Documents")
   st.text('This is some text. This is some text. This is some text.')
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
