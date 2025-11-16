# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# opts = webdriver.ChromeOptions()
# prefs = {
#         "credentials_enable_service": False,
#         "profile.password_manager_enabled": False
#     }
# opts.add_experimental_option("prefs", prefs)
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)

# driver.get("https://www.saucedemo.com/")
# driver.find_element(By.CSS_SELECTOR, "[data-test='username']").send_keys("standard_user")
# driver.find_element(By.ID, "password").send_keys("secret_sauce")
# driver.find_element(By.ID, "login-button").click()

# # products = driver.find_elements(By.XPATH, '//div[@data-test="inventory-item"]')
# # print(len(products))
# # for product in products:
# #     print(product.text)

# driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']").click()
# # print("Current URL:", driver.current_url)

# driver.back()
# driver.find_element(By.LINK_TEXT, "Twitter").click()
# print(driver.current_url)
# handles = driver.window_handles # list of window ids that are currently open
# print(handles)
# # print(driver.current_window_handle)
# time.sleep(5)
# driver.switch_to.window(handles[1])
# print(driver.current_url)

