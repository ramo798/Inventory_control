import gspread
from oauth2client.service_account import ServiceAccountCredentials


# sheetへの接続処理
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('mykey.json', scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = '14KEmq_Ziqf5DyB7im6-sNECmHeGR4GEio_KYPTw8R-Q'
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

try:
    being = worksheet.find('a')
except gspread.exceptions.CellNotFound:
    print("erro")
