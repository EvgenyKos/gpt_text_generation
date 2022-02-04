import streamlit as st
from gsheetsdb import connect

def app(tool, prompt, upvote):

    
    st.title(tool)

    st.metric(label='', value=int(upvote), delta = 'upvotes')

    with st.form("text_gen"):
        prod_name = st.text_input("Product name", "")
        prod_func = st.text_area("What your product does", height=200)
        if st.form_submit_button("Generate text"):
            st.write('hi there')

    generated_text = st.empty()