import streamlit  as st
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=SCOPES)

SPREADSHEET_ID = st.secrets['sheet_id']

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()

def read_db():
    result_input = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range='Tools!A1:C100').execute()
    values_input = result_input.get('values', [])
    return values_input

def write_df(value_input, sheet):
    result = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID, range='Tools!A1:C1',
            valueInputOption='USER_ENTERED',
            insertDataOption = 'INSERT_ROWS',
                body = {'values':value_input} ).execute()

    pass

def upvote_gs(value, index):
    result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID, range=f'Tools!C{index+1}',
            valueInputOption='USER_ENTERED',
            body = {'values':[[int(value)+1]]} ).execute()
    pass

def devote_gs(value, index):
    result = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID, range=f'Tools!C{index+1}',
            valueInputOption='USER_ENTERED',
            body = {'values':[[int(value)-1]]} ).execute()
    pass