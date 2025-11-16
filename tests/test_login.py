from source_page.login_page import LoginPage
import pytest

@pytest.mark.parametrize("username, password, expected", [("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "locked"),("invalid_user", "wrong_pass", "fail")])


def test_valid_login(driver, username, password, expected):
    login = LoginPage(driver)
    login.open() 
    login.login(username, password)


    if expected == "success":
        assert "inventory" in driver.current_url, "Login is failed"



























































# from login_page import LoginPage


# class TestLogin:
#     def test_valid_login(self, driver):
#         login = LoginPage(driver)
#         login.open()
#         login.login("standard_user", "secret_sauce")
#         assert "inventory" in driver.current_url 

#     def test_invalid_login(self, driver):
#         login = LoginPage(driver)
#         login.open()
#         login.login("invalid_user", "wrong_pass")
#         error = driver.find_element("css selector", "[data-test='error']").text
#         assert "Epic sadface" in error  

#     def test_blank_fields(self, driver):
#         login = LoginPage(driver)
#         login.open()
#         login.login("", "")
#         error = driver.find_element("css selector", "[data-test='error']").text
#         assert "Username is required" in error
