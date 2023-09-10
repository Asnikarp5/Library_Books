import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(credentials)

sheet = client.open("library_books")

title = sheet.worksheet("list")

data = title.get_all_values()

print(data)