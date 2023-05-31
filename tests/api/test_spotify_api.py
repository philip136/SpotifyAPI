import pytest

from utils.provider import SpotifyProvider
from utils.constant import ArtistNameConstant, GenreConstant, SongConstant


class TestSpotifyAPI:
    provider: SpotifyProvider = SpotifyProvider()

    @pytest.mark.parametrize(
        "artist_name, expected_genre",
        [
            pytest.param(ArtistNameConstant.DRAKE, GenreConstant.RAP),
            pytest.param(ArtistNameConstant.THE_BEATLES, GenreConstant.BRITISH_INVASION)
        ]
    )
    def test_check_genre(self, artist_name: str, expected_genre: str):
        """Make sure the artist has a specific genre."""
        artists = self.provider.find_artists_by_name(artist_name=artist_name)
        certain_artist = next(filter(lambda artist: artist.name.lower() == artist_name.lower(), artists))
        assert expected_genre in certain_artist.genres, f"The artist does not have a genre of {expected_genre}"

    @pytest.mark.parametrize(
        "artist_name, expected_song",
        [
            pytest.param(ArtistNameConstant.DRAKE, SongConstant.ONE_DANCE),
            pytest.param(ArtistNameConstant.THE_BEATLES, SongConstant.HERE_COMES_THE_SUN)
        ]
    )
    def test_check_the_most_popular_song(self, artist_name: str, expected_song: str):
        """Make sure the artist has the next popular song."""
        artists = self.provider.find_artists_by_name(artist_name=artist_name)
        certain_artist = next(filter(lambda artist: artist.name.lower() == artist_name.lower(), artists))
        top_tracks = self.provider.find_top_tracks_by_artist(artist=certain_artist)
        track_exists = bool([track for track in top_tracks if track.name.lower() == expected_song.lower()])
        assert track_exists, f"The song {expected_song} is not popular song"

