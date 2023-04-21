import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Demo App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


pdf = Image.open('pdf.png')
docx = Image.open('docx.png')

files =['Corporate Social Responsibility Policy.pdf','Standard Corporate Social Responsibility Policy.pdf','Activities in Corporate Social Responsibility Policy.pdf',
       'Environment Protection Program Policy.pdf','Work Health and Safety Culture Policy.pdf','Client Complaint Management Policy.pdf',
       'Basic Complaint Management Policy.pdf','Anti-Harassement Policy and Procedure.pdf','General Information Technology Policy.pdf','Nondiscrimination Policy.pdf',
       'Air - Environment protection policy.docx']

colsize = [0.2,2,1,3,4]
cols = st.columns(colsize)
cols[0].write("")
cols[1].write("Documents")
cols[2].write('')
cols[3].write('Topic')
cols[4].write('Content')
for i in files:
    cols = st.columns(colsize)
    if i.endswith('pdf'):        
        cols[0].image(pdf)
    else:
        cols[0].image(docx)
    cols[1].write(i)
    cols[2].write('VIEW|ANALYSE')
    cols[3].write('x')
    cols[4].write('x')
st.button('ANAYLSE')
