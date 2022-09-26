from selenium import webdriver as wd
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def pytest_addoption(parser):
    parser.addoption("--remote", action="store")


@pytest.fixture(autouse=True)
def driver(request):
    if request.config.getoption('--remote'):
        from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
        driver = wd.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
    else:
        driver = wd.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


