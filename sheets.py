"""
BEFORE RUNNING:
---------------
1. If not already done, enable the Google Sheets API
   and check the quota for your project at
   https://console.developers.google.com/apis/api/sheets
2. Install the Python client library for Google APIs by running
   `pip install --upgrade google-api-python-client`
"""
from pprint import pprint
import os
from oauth2client import file, client, tools
from googleapiclient import discovery
from httplib2 import Http

# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
scopes = 'https://www.googleapis.com/auth/spreadsheets'
path = os.path.abspath(os.pardir) + '/credentials/sheets.json'
store = file.Storage(path)
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(path, scopes)
    creds = tools.run_flow(flow, store)

service = discovery.build('sheets', 'v4', http=creds)


# The ID of the spreadsheet to update.
spreadsheet_id = '107RYI3yNbn3NPRj-usYNWP6mLtP9yzPJ2uImAHVzO2o'  # TODO: Update placeholder value.

# The A1 notation of the values to update.
range_ = 'A1:A1'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 'RAW'  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body. All existing entries
    # will be replaced.
}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)