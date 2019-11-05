import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

def authenticate(url='https://docs.google.com/spreadsheets/d/107RYI3yNbn3NPRj-usYNWP6mLtP9yzPJ2uImAHVzO2o/'):
    scope = ['https://spreadsheets.google.com/feeds']
    path = os.path.abspath(os.pardir) + '/credentials/menu.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(path, scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(url)
    return sheet

def write(sheet, row, col, s):
    sheet.sheet1.update_cell(row, col, s)

if __name__ == '__main__':
    sheet = authenticate(url='https://docs.google.com/spreadsheets/d/107RYI3yNbn3NPRj-usYNWP6mLtP9yzPJ2uImAHVzO2o/').sheet1
    write(sheet, 3, 5, 'asdf\nadsf')
