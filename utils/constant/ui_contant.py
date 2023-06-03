from typing import Tuple

from selenium.webdriver.common.by import By


class UrlConstant:
    SPOTIFY_HOME_PAGE: str = "https://open.spotify.com/"


class LocatorConstant:
    FORM_ROOT_LOCATOR: Tuple[By, str] = (By.XPATH, "div[data-testid='root']")
    NAVBAR_BTN_LOCATOR: Tuple[By, str] = (By.XPATH, "//span[contains(text(),'%s')]")
    SONG_TEXT_BOX_LOCATOR: Tuple[By, str] = (By.XPATH, "//form//input[@data-testid='search-input']")
    SINGER_BTN_LOCATOR: Tuple[By, str] = (By.CSS_SELECTOR, "div[data-testid='herocard-click-handler']")
    SONG_LOCATOR: Tuple[By, str] = (By.XPATH, "//div[contains(text(),'%s')]")
    ROOT_LOCATOR: Tuple[By, str] = (By.CSS_SELECTOR, "//div[@data-testid='root']")
    RECENT_SEARCH_SINGER: Tuple[By, str] = (
        By.XPATH, "//section[@aria-label='Recent searches']//div[@data-testid='grid-container']/div"
    )


class ElementNameConstant:
    SINGER_PAGE_FORM: str = "Singer Page Form"
    SEARCH_BTN: str = "Search"
    SONG_TEXT_BOX: str = "Song TextBox"
    SINGER_BTN: str = "Singer Button"
    SONG_LINK: str = "Song Link"
    ROOT_NAME: str = "Root"
    RECENT_SINGERS: str = "Recent singers"
