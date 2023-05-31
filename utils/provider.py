import os
import random
import base64
from urllib.parse import urlencode
from requests.sessions import Session
from typing import List

from models.artist import Artist
from models.album import Album
from models.track import Track
from utils.constant import HttpStatusCodeConstant, EndPointConstant


class SpotifyProvider:
    _session: Session

    @staticmethod
    def __get_client_credentials() -> str:
        client_id, client_secret = os.environ.get("client_id"), os.environ.get("client_secret")
        if not any([client_id, client_secret]):
            raise ConnectionAbortedError("'client_id' and 'client_secret' were not found for the Spotify account")
        client_credentials = f"{client_id}:{client_secret}"
        return base64.b64encode(client_credentials.encode()).decode()

    @property
    def session(self) -> Session:
        if not hasattr(self, "_session"):
            self._session = Session()
            response = self._session.post(
                EndPointConstant.BASE_TOKEN_ENDPOINT,
                data={"grant_type": "client_credentials"},
                headers={"Authorization": f"Basic {self.__get_client_credentials()}"}
            )
            assert response.status_code == HttpStatusCodeConstant.OK, "Failed to login"
            auth_data = response.json()
            self._session.headers.update({"Authorization": f"{auth_data['token_type']} {auth_data['access_token']}"})
        return self._session

    def find_available_markets(self) -> List[str]:
        response = self.session.get(EndPointConstant.AVAILABLE_MARKETS_ENDPOINT)
        return response.json()["markets"]

    def find_artists_by_name(self, artist_name: str) -> List[Artist]:
        query_data = urlencode({"q": artist_name, "type": "artist"})
        response = self.session.get(f"{EndPointConstant.SEARCH_ENDPOINT}{query_data}")
        assert response.status_code == HttpStatusCodeConstant.OK, "Failed to get artist data"
        artist_list = response.json()["artists"]["items"]
        return [Artist.create_model(artist_data) for artist_data in artist_list]

    def find_certain_artist(self, artist_name: str):
        return next(filter(lambda artist: artist.name == artist_name, self.find_artists_by_name(artist_name)))

    def find_top_tracks_by_artist(self, artist: Artist) -> List[Track]:
        query_data = urlencode({"market": random.choice(self.find_available_markets())})
        response = self.session.get(f"{EndPointConstant.BASE_API_ENDPOINT}/artists/{artist.id}/top-tracks?{query_data}")
        top_tracks = response.json()["tracks"]
        for top_track in top_tracks:
            top_track["album"] = Album.create_model(top_track["album"])
        return [Track.create_model(track_data) for track_data in top_tracks]






