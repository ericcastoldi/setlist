

class SpreadsheetSetlists:

    def __init__(self, google_sheets):
        self._google_sheets = google_sheets

    def get_setlist(self, spreadsheet_id='1fl9nsCZlc8vUxl8oMYRVblOuYdMcrQARAH4B4B32BDs'):
        spreadsheet = self._google_sheets.open_by_key(spreadsheet_id)
        worksheet = spreadsheet.get_worksheet(1)
        songs = worksheet.col_values(1)
        artists = worksheet.col_values(2)

        setlist = []
        for idx in range(len(songs)):
            setlist.append({ 'song': songs[idx], 'artist': artists[idx]})

        return setlist[1:]