import streamlit as st
from main import blog_writer

st.set_page_config("Blog Writer")

st.title("Blog Writer")

company_details = st.text_area("Enter Company details:")
topic_name = st.text_input("Enter Topic Name:")
target_audience = st.text_input("Enter the target audience:")

if st.button("Submit"):
    with st.spinner("Generating blog content..."):
        st.write(blog_writer(company_details, topic_name, target_audience))


