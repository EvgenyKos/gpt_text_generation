import streamlit as st
from functions import *
from googl_sheet import *


def app(key):

    if "g_text" not in st.session_state:
        st.session_state.g_text = ""

    set_openai_key(key)

    st.title("Create tool")
    form = st.form('Create tool')
    tool_name = form.text_input("Tool name", "for example: Website headline")
    prompt = form.text_area("Type the prompt to genarte text", height=200)

    if form.form_submit_button("Generate text"):
        with st.spinner("Generating text..."):
            resp = gpt_3(prompt, 0.5, "text-ada-001")
            st.session_state.g_text = resp['choices'][0]['text']
            st.markdown(resp['choices'][0]['text'])

    if st.button("Save tool"):
        final_prompt = f"Input: {prompt}. \nOutput: {st.session_state.g_text}"
        value_input = [[tool_name, final_prompt, 0]]
        write_df(value_input)
        st.success("Tool saved")
        