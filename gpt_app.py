import streamlit as st
import create_tool
import text_gen
import YC_apl
import pandas as pd
from functions import *
from googl_sheet import *

st.set_page_config(
    page_title="Creative writing tool",
    page_icon="🖊️",
    layout="centered")

@st.cache
def get_dictionary(values):
    df = pd.DataFrame(values)
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    tools = {}
    for index, row in df.iterrows():
        tools[row['tool']] = [row['prompt'], row['upvote'], index]
    return tools

def create_state():
    st.session_state.create=True

def change_tool():
    st.session_state.create=False

if 'create' not in st.session_state:
    st.session_state.create=False

values = read_db()
tools = get_dictionary(values)


#Sort bases on upvote
tools = dict(sorted(tools.items(), key=lambda item: item[1][1], reverse=True))

api_key = st.sidebar.text_input("OpenAI API Key:", type="password", help="Get your API key from https://openai.com/api")
st.sidebar.markdown("No text will be generated without OpenAI key")

but_tool = st.sidebar.empty()

st.sidebar.markdown("## Select tool")
option = st.sidebar.radio("", tools.keys(), on_change=change_tool)

but_tool.button("Create tool", on_click=create_state)

if st.session_state.create:
    create_tool.app(api_key)
else:

    tool = tools[option]
    if option=="YC":
        YC_apl.app(tool[1], tool[2], api_key)
    else:
        text_gen.app(option, tool[0], tool[1], tool[2], api_key)
