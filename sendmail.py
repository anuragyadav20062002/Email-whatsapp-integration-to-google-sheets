from re import sub
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import smtplib

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
                            range="sheet1!B2:B5").execute()
values = result.get('values', [])

# sending email procedure

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("anuragyadavexperiments@gmail.com", "#0987654321abc")
msg = "Hello this is a email form python"
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)

# now mapping the emails

for i in values:
    server.sendmail("anuragyadavexperiments@gmail.com", i, body)
server.quit()

