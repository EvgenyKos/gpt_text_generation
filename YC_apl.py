from click import prompt
import streamlit as st
import openai
from functions import *
from googl_sheet import *


def app(key):

    base_prompt = """
    Input: Write the answer for the following Y Combinator application question for my startup OpenPhone that is a phone system equipped with CRM capabilities, built from the ground up to fit the needs of small businesses.
    """ 

    start_prompt = "Input: Write the answer for the following Y Combinator application question for my startup "

    set_openai_key(key)

    st.title("YC application")

    prod_name = st.text_input("Company name", "")
    prod_func = st.text_area("What your product does and who it is for.", "")
    #length = st.slider("Length", 1, 2048, 2048)
    engine = st.selectbox("Engine", ["text-davinci-001", "text-curie-001", "text-babbage-001", "text-ada-001"], help="See OpenAI pricing at https://openai.com/api/pricing")
    temper = st.slider("Creativity", 0.0, 1.0, 0.7)

    st.markdown("**Questions**")
    with st.expander("Describe what your company does in 50 characters or less."):
        question1 = """Describe what your company does in 50 characters or less.
                    """     
        answer1 = """Phone system meets CRM built for small businesses
        """
        final_prompt = f"{base_prompt} \nQuestion: {question1} \nAnswer: {answer1} \n\n{start_prompt} that is {prod_func}. \n\nQuestion: {question1} \nAnswer: "
        if st.button("Generate ideas"):
            for i in range(3):
                resp = gpt_3(final_prompt, temper, engine, 1000)
                st.markdown(f"Option {i+1}:")
                st.success(resp['choices'][0]['text'])
                st.write(f"Reponse length (in characters): {len(resp['choices'][0]['text'])}")

    with st.expander("What is your company going to make?"):
        question2 = """What is your company going to make? Please describe your product and what it does or will do.
                    """     
        answer2 = """We're making a phone system equipped with CRM capabilities, built from the ground up to fit the needs of small businesses.
        Through our mobile application, small business owners get a simple yet powerful business phone system with a dedicated phone number on top of their existing mobile devices.
        We are not just another phone system though. We start by owning the communication channel and then use that data to help small businesses communicate better and earn more money.
        """
        final_prompt2 = f"{base_prompt} \nQuestion: {question2} \nAnswer: {answer2} \n\n{start_prompt}{prod_name} that is {prod_func}. \n\nQuestion: {question2} \nAnswer: "
        if st.button("Generate answer"):
            for i in range(3):
                resp = gpt_3(final_prompt2, temper, engine, 1600)
                st.markdown(f"Option {i+1}:")
                st.info(resp['choices'][0]['text'])
                st.write(f"Reponse length (in characters): {len(resp['choices'][0]['text'])}")

    with st.expander("Rephase your answer"):
        re_text = st.text_area("Type sentence(s) you want to rephrase", "", height=250)
        final_prompt3 = f"Input: Rephrase the following sentence(s): {re_text} \nOutput:"
        if st.button("Rephrase"):
            for i in range(3):
                resp = gpt_3(final_prompt3, temper, engine, 1600)
                st.markdown(f"Option {i+1}:")
                st.info(resp['choices'][0]['text'])
                st.write(f"Reponse length (in characters): {len(resp['choices'][0]['text'])}")
