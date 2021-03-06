import base64
import requests

def spotify_auth():
    client_id = '2a37ebbb434e4ce09b406d0d34b9ca9a'
    client_secret = '742dc8ae817044e7b5bd66393a524e62'
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
