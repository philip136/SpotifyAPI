class EndPointConstant:
    BASE_API_ENDPOINT: str = "https://api.spotify.com/v1"
    BASE_TOKEN_ENDPOINT: str = "https://accounts.spotify.com/api/token"
    AVAILABLE_MARKETS_ENDPOINT: str = f"{BASE_API_ENDPOINT}/markets"
    SEARCH_ENDPOINT: str = f"{BASE_API_ENDPOINT}/search?"


class HttpStatusCodeConstant:
    OK: int = 200


class ArtistNameConstant:
    DRAKE: str = "Drake"
    THE_BEATLES: str = "The beatles"


class GenreConstant:
    BRITISH_INVASION: str = "british invasion"
    RAP: str = "rap"


class SongConstant:
    ONE_DANCE: str = "One Dance"
    HERE_COMES_THE_SUN: str = "Here Comes The Sun - Remastered 2009"
