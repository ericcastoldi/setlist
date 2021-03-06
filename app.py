import os
import base64
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from spotipy import Spotify, SpotifyOAuth

def get_spreadsheet_songs():
    spreadsheet_id = '1fl9nsCZlc8vUxl8oMYRVblOuYdMcrQARAH4B4B32BDs'
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('setlist-backend-ebbead78f0a0.json', scope)
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.get_worksheet(1)
    songs = worksheet.col_values(1)
    artists = worksheet.col_values(2)

    setlist = []
    for idx in range(len(songs)):
        setlist.append({ 'song': songs[idx], 'artist': artists[idx]})

    setlist = setlist[1:]
    print(setlist)
    return setlist

def spotipy_playlist():
    scope = 'playlist-modify-public'
    username = 'fod4mstb1n1qgwvffe3ac52dd'
    oauth = SpotifyOAuth(
        scope=scope, 
        username=username, 
        client_id=os.environ['SPOTIFY_CLIENT_ID'], 
        client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
        redirect_uri='https://google.com'
    )

    token_dict = oauth.get_access_token()
    token = token_dict['access_token']

    spotify = Spotify(auth=token)
    playlist = spotify.user_playlist_create(
        user=username, 
        name='Setlist auto playlist', 
        public=True, 
        description='API Generated Playlist Test'
    )

    print(playlist)
    playlist_id = playlist['id']

    setlist = get_spreadsheet_songs()
    tracks = []
    for item in setlist:
        search_result = spotify.search(q=f'artist:{item["artist"]} track:{item["song"]}', limit=1)
        print(search_result)
        try:
            tracks.append(search_result['tracks']['items'][0]['uri'])
        except:
            pass
    
    spotify.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=tracks)
        


spotipy_playlist()
print('OK')
