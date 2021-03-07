from app import SpotifyPlaylists, SpotifyAuthenticator, SpreadsheetAuthenticator, SpreadsheetSetlists

def create_playlist():
    spreadsheet_setlists =  SpreadsheetSetlists(SpreadsheetAuthenticator().authenticate())
    setlist = spreadsheet_setlists.get_setlist()

    spotify_playlists = SpotifyPlaylists(SpotifyAuthenticator().authenticate())
    spotify_playlists.create(setlist=setlist)


create_playlist()

print('OK')
