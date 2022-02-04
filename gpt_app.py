from webbrowser import get
import streamlit as st
import create_tool
import text_gen
from gsheetsdb import connect
import pandas as pd

public_gsheets_url = "https://docs.google.com/spreadsheets/d/15bkGywUo6ru8Fczi03_0XufLw-_rfG7SM-j6WjiiGvM/edit#gid=0"

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
#@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    return rows

#sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{public_gsheets_url}"')

@st.cache
def get_dictionary(rows):
    df = pd.DataFrame(rows)
    tools = {}
    for index, row in df.iterrows():
        tools[row['tool']] = [row['prompt'], row['upvote']]
    return tools

tools = get_dictionary(rows)

st.sidebar.title("Tools")

df = pd.DataFrame(rows)


option = st.sidebar.radio("", tools.keys())


if st.sidebar.button("Create tool"):
    create_tool.app()
else:

    tool = tools[option]

    text_gen.app(option, tool[0], tool[1])