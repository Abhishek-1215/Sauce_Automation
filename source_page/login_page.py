from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.log_btn = (By.ID, "login-button")


    def open(self):
        self.driver.get("https://www.saucedemo.com/")


    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.log_btn).click()


    

