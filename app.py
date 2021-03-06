import os
import base64
import requests
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth

def spotipy_playlist():
    scope = 'playlist-modify-public'
    username = 'fod4mstb1n1qgwvffe3ac52dd'
    token = SpotifyOAuth(
        scope=scope, 
        username=username, 
        client_id=os.environ['SPOTIFY_CLIENT_ID'], 
        client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
        redirect_uri='http://127.0.0.1:8080'
    )
    spotify = Spotify(auth_manager=token)

    spotify.user_playlist_create(user=username, name='Setlist auto playlist', public=True, description='API Generated Playlist Test')

spotipy_playlist()


def spotify_auth():
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
    client_credentials = f'{client_id}:{client_secret}'
    encoded_credentials = base64.b64encode(client_credentials.encode())

    token_url = 'https://accounts.spotify.com/api/token'
    token_data = {
        'grant_type': 'client_credentials'
    }

    token_headers ={
        'Authorization': f'Basic {encoded_credentials.decode()}'
    }

    response = requests.post(token_url, data=token_data, headers=token_headers)
    response_data = response.json()

    access_token = response_data['access_token']
    return access_token

