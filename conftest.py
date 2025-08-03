import pytest
import allure
from selenium import webdriver
from src.config import Config
from pages.main_page import MainPage
from selenium.webdriver.firefox.options import Options

@pytest.fixture
def driver():

    firefox_options = Options()
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(options=firefox_options)

    if Config.MAXIMIZE:
        driver.maximize_window()
    else:
        driver.set_window_size(Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT)

    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver).open()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )