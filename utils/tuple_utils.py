from typing import Tuple

from selenium.webdriver.common.by import By


def fill_locator_value(value: str, locator: Tuple[By, str]) -> Tuple[By, str]:
    locator_strategy, locator_value = locator
    locator_value = locator_value % value
    return locator_strategy, locator_value
