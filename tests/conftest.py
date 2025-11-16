import pytest
from selenium import webdriver
from source_page.login_page import LoginPage

@pytest.fixture(scope="function")
def driver():
    opts = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opts)

    yield driver

    driver.quit()


@pytest.fixture()
def logged_in_driver(driver):
    login = LoginPage(driver)
    login.open() 
    login.login("standard_user", "secret_sauce")
    return driver