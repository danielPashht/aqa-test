import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Locators:
    logo = (By.XPATH, '//img')
    codes_menu = (By.XPATH, "//ul[@id='navMenu']/li[1]/a[@href='#']")
    search_input = (By.XPATH, "/html//input[@id='searchText']")
    search_button = (By.XPATH, "/html//button[@id='search']")
    codes_icd10_option = (By.XPATH, '//*[@id="navMenu"]/li[1]/ul/li[1]/a')


@pytest.mark.usefixtures('driver')
class SearchPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.open()

    def open(self):
        self.driver.get('https://www.icd10data.com/')

    def verify_logo(self):
        if self.driver.find_element(*Locators.logo):
            return True
        else:
            return False

    def open_codes_menu(self):
        self.driver.find_element(*Locators.codes_menu).click()

    def click_icd_10_option(self):
        self.driver.find_element(*Locators.codes_icd10_option).click()

    def fill_field(self, locator, value: str) -> None:
        self.driver.find_element(*locator).send_keys(value)

    def search(self, value: str) -> None:
        self.driver.find_element(*Locators.search_input).send_keys(value)
        self.driver.find_element(*Locators.search_button).click()

    def search_value_displayed(self, value: str) -> bool:
        if self.driver.find_element(By.XPATH, f'//span[text()="{value}"]'):
            return True
        else:
            return False
