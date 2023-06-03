class EndPointConstant:
    BASE_API_ENDPOINT: str = "https://api.spotify.com/v1"
    BASE_TOKEN_ENDPOINT: str = "https://accounts.spotify.com/api/token"
    AVAILABLE_MARKETS_ENDPOINT: str = f"{BASE_API_ENDPOINT}/markets"
    SEARCH_ENDPOINT: str = f"{BASE_API_ENDPOINT}/search?"


class HttpStatusCodeConstant:
    OK: int = 200

