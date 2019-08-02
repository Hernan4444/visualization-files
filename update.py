import os
import pickle
from googleapiclient.discovery import build
from dotenv import load_dotenv
from pathlib import Path  # python3 only
import sys

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

ID = "1Wevi-zEFdbNymlPeVVvgsAcVlQl_s8oROQHo2R3K-tc"
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
        Credentials, the obtained credential.
    """
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
    return creds


def get_sheet_info():

    credentials = get_credentials()
    service = build('sheets', 'v4', credentials=credentials)


    spreadsheetId = ID

    values = service.spreadsheets().get(spreadsheetId=spreadsheetId,
                                        ranges=[],
                                        includeGridData=False)
    values = values.execute()

    rangeName = values["sheets"][0]['properties']['title']
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        print('No data found.')
    else:
        return values

data = get_sheet_info()
with open("Registro.csv", "w", encoding="UTF-8") as file:
    for line in data:
        file.write(";".join(line) + "\n")

user = sys.argv[1]
password = sys.argv[2]
repo = sys.argv[3]

os.system("python3 cursos_uc_csv_to_json.py")
os.system("git status")
os.system("git add .")
os.system('git commit -m "automatic update"')
os.system('git push https://{}:{}@{} --all'.format(user, password, repo))