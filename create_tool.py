import streamlit as st
from gsheetsdb import connect


def app():

    st.title("Create tool")

    prompt = st.text_area("Type the prompt to genarte text", height=200)

    if st.button("Generate text"):
        with st.spinner("Generating text..."):
            st.markdown("Hi, I'm a generated text")
        
        tool_name = st.text_input("Tool name", "")