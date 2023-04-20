import streamlit as st
from PIL import Image

pdf = Image.open('pdf.png')
docx = Image.open('docx.png')


col0, col1, col2, col3 = st.columns([1,10,3,3],gap="small")

with col0:
   st.subheader("__")
   st.image(pdf, use_column_width='auto')
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(pdf, width=15)
   st.image(docx, width=15)
with col1:
   st.subheader("Documents")
   st.text('Corporate Social Responsibility Policy.pdf')
   st.text('Standard Corporate Social Responsibility Policy.pdf')
   st.text('Activities in Corporate Social Responsibility Policy.pdf')
   st.text('Environment Protection Program Policy.pdf')
   st.text('Work Health and Safety Culture Policy.pdf')
   st.text('Client Complaint Management Policy.pdf')
   st.text('Basic Complaint Management Policy.pdf')
   st.text('Anti-Harassement Policy and Procedure.pdf')
   st.text('General Information Technology Policy.pdf')
   st.text('Nondiscrimination Policy.pdf')
   st.text('Air - Environment protection policy.docx')
   
with col2:
   st.subheader("Topics")
   st.text('This is some text.')

with col3:
   st.subheader("Content")
