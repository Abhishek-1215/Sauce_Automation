import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.social_media_links = {
            "twitter": (By.LINK_TEXT, "Twitter"),
            "facebook": (By.LINK_TEXT, "Facebook"),
            "linkedin": (By.LINK_TEXT, "LinkedIn"),
        }

    # locators
    title_text = (By.XPATH, "//div[@class='app_logo']")
    inventory_item = (By.XPATH, '//div[@data-test="inventory-item"]')
    cart_badge = (By.XPATH, "//span[@class='shopping_cart_badge']")
    add_to_cart_btn = (By.XPATH, "//button[contains(normalize-space(),'Add to cart')]")
    remove_btn = (By.XPATH, "//button[contains(text(),'Remove')]")
    cart_page = (By.XPATH, "//a[@class='shopping_cart_link']")
    burger_menu = (By.XPATH, "//button[@id='react-burger-menu-btn']")
  

    def get_page_title(self):
        return self.driver.find_element(*self.title_text).text

    def get_product_count(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.inventory_item)
        )
        return len(self.driver.find_elements(*self.inventory_item))

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_btn).click()

        return self.driver.find_element(*self.cart_badge).text

    def remove_frm_cart(self):
        self.driver.find_element(*self.remove_btn).click()
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, "[data-testid='shopping-cart-badge']")))
        return True
    
    def get_cart_page(self):
        time.sleep(5)
        self.driver.find_element(*self.cart_page).click()
        time.sleep(10)
        return self.driver.current_url

    def validate_social_media_links(self, soc_media):
        if soc_media not in self.social_media_links:
            raise ValueError(f"Unknown social media :", {soc_media})
        main_url = self.driver.current_url
        locator = self.social_media_links[soc_media]
        self.driver.find_element(*locator).click()
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])
        new_url = self.driver.current_url
        
        self.driver.close()
        self.driver.switch_to.window(main_url)
        return new_url
    

    def get_menu_options(self):
        self.driver.find_element(*self.burger_menu).click()


    def is_burger_menu_opened(self):
        try:
            menu = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='about_sidebar_link']")))
            return menu.is_displayed()
        except:
            return False