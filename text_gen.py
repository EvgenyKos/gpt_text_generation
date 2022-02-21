import streamlit as st
from functions import *
from googl_sheet import *

def app(tool, prompt, upvote, index, key):

    set_openai_key(key)

    st.title(tool)
    #length = st.slider("Length", 1, 2048, 2048)
    engine = st.selectbox("Engine", ["text-davinci-001", "text-curie-001", "text-babbage-001", "text-ada-001"], help="See OpenAI pricing at https://openai.com/api/pricing")
    temper = st.slider("Creativity", 0.0, 1.0, 0.7)

    col1, col2 = st.columns([5,1])

    col2.metric(label='', value=int(upvote), delta = 'upvotes')
    place_but = col2.empty()
    if place_but.button("+1", on_click=lambda: upvote_gs(upvote, index)):
        if place_but.button("-1", on_click=lambda: devote_gs(upvote, index)):
            pass

    with col1:
        form = st.form("text_gen")
        prod_name = form.text_input("Product name", "")
        prod_func = form.text_area("What your product does", height=200, help = "Provide more details.")
        final_prompt = f"{prompt} \nInput: Write {tool} for {prod_name} that is {prod_func}. \nOutput: "
        # st.text(final_prompt)
        if form.form_submit_button("Generate text"):

            for i in range(3):
                resp = gpt_3(final_prompt, temper, engine, 1800)
                st.markdown(f"Option {i+1}:")
                st.info(resp['choices'][0]['text'])
            

