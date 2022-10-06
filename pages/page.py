import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Locators:
    locator = (By.CSS_SELECTOR, 'locator')


@pytest.mark.usefixtures('driver')
class Page:

    url = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.open()

    def open(self):
        self.driver.get(self.url)

    def fill_field(self, locator, value: str) -> None:
        self.driver.find_element(*locator).send_keys(value)

