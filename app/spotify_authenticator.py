from os import environ
from spotipy import Spotify, SpotifyOAuth

class SpotifyAuthenticator:

    def __init__(self, ):
        self._client_id = environ['SPOTIFY_CLIENT_ID']
        self._client_secret = environ['SPOTIFY_CLIENT_SECRET']

    def authenticate(self, scope='playlist-modify-public', username='fod4mstb1n1qgwvffe3ac52dd'):
        oauth = SpotifyOAuth(
            scope=scope, 
            username=username,     
            client_id=self._client_id, 
            client_secret=self._client_secret,
            redirect_uri='https://google.com'
        )

        token_dict = oauth.get_access_token()
        token = token_dict['access_token']

        return Spotify(auth=token)
