import os
import base64
import requests



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

spotify_auth()
