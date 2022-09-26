from pages.search import SearchPage


def test_verify_logo_displayed(driver):
    page = SearchPage(driver)
    assert page.verify_logo()


def test_codes_menu_opens(driver):
    page = SearchPage(driver)
    page.open_codes_menu()
    page.click_icd_10_option()
    assert page.driver.current_url == 'https://www.icd10data.com/ICD10CM/Codes'


def test_search_covid(driver):
    page = SearchPage(driver)
    page.search('U07.1')
    assert page.search_value_displayed('U07.1')
