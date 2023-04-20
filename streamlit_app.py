import streamlit as st
from PIL import Image

image = Image.open('pdf.png')


col0, col1, col2, col3 = st.columns([1,3,3,3],gap="small")

with col0:
   st.subheader("")
   st.image(image, width=10)
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
