import logging

class SpotifyPlaylists:

    _username = 'fod4mstb1n1qgwvffe3ac52dd'

    def __init__(self, spotify):
        self._spotify = spotify
        self._logger = logging.getLogger(__name__)

    def create(self, name=None, description=None, setlist=None):
        playlist = self._spotify.user_playlist_create(
            user=self._username, 
            name=name or 'Setlist auto playlist', 
            public=True, 
            description=description or 'API Generated Playlist Test'
        )

        self.add_songs(playlist['id'], setlist)

    def add_songs(self, playlist_id, setlist):
        if not setlist:
            return

        tracks = list(filter(
            lambda track_item: track_item is not None, 
            map(
                lambda setlist_item: self._get_track_id(setlist_item), 
                setlist
            )
        ))

        add_tracks_response = self._spotify.user_playlist_add_tracks(
            user=self._username, 
            playlist_id=playlist_id, 
            tracks=tracks
        )

        self._logger.info(add_tracks_response)
    
    def _get_track_id(self, setlist_item):
        query = f'artist:{setlist_item["artist"]} track:{setlist_item["song"]}'
        search_result = self._spotify.search(
            q=query, 
            limit=1
        )

        self._logger.info(search_result)
        
        try:
            setlist_item_description = f'{setlist_item["artist"]} - {setlist_item["song"]}'
            if len(search_result['tracks']['items']) == 0:
                self._logger.warn(f'{setlist_item_description} not found.')
                return None

            track_uri = search_result['tracks']['items'][0]['uri']
            
            self._logger.info(
                f'{setlist_item_description} found with spotify uri: {track_uri}'
            )

            return track_uri
        except Exception as ex:
            msg = f'{setlist_item_description}: {str(ex)}'
            self._logger.error(msg)
            return None
            
