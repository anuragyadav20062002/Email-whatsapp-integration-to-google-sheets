from googleapiclient.discovery import build
from google.oauth2 import service_account
import pywhatkit as py
import datetime

SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of spreadsheet.
SAMPLE_SPREADSHEET_ID = '1idZsr-kgNhF_Jo31auDNMl-pYbEE94Cck1uB3A5urEY'

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range="sheet1!C2:C5").execute()
values = result.get('values', [])

print(values)

# Sensing Whatsapp Messages

now = datetime.datetime.now();
min= now.minute+1 
hour = now.hour

for i in values:

    py.sendwhatmsg('+'+i[0], "Hi, there this is an auto generated message by pyhton please ignore this", hour,min)
    min=min+1