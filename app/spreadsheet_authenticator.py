import gspread
from oauth2client.service_account import ServiceAccountCredentials

class SpreadsheetAuthenticator:

    def __init__(self):
        self._scope = ['https://spreadsheets.google.com/feeds']

    def authenticate(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            'setlist-backend-ebbead78f0a0.json', 
            self._scope
        )
        
        return gspread.authorize(credentials)
