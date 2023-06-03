import pytest

from browser.browser import Browser
from browser.py_quality_services import PyQualityServices


@pytest.fixture(scope="session")
def browser() -> Browser:
    browser = PyQualityServices.get_browser()
    browser.maximize()
    yield browser
    browser.quit()
