import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
   st.header("Documents")
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:', run_sentiment_analysis(txt))

with col2:
   st.header("Topics")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("Content")
