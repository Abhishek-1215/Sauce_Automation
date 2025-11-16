from selenium.common import NoSuchElementException

from source_page.product_page import ProductPage


def test_product(logged_in_driver):
    inventory = ProductPage(logged_in_driver)
    
    assert inventory.get_page_title() == "Swag Labs", "Page title mismatch"

    
    assert inventory.get_product_count() == 6, "Product count is wrong"

    assert inventory.add_to_cart() == "1", "Cart count after adding is wrong"

    assert inventory.remove_frm_cart(), "Cart count after adding is wrong"
    
    # inventory.get_cart_page()
    # assert "cart" in logged_in_driver.current_url, "Cart page navigation is not accurate"

    
    inventory.validate_social_media_links("twitter")
    assert "https://x.com/saucelabs" in logged_in_driver.current_url, "page navigation is wrong"

    inventory.validate_social_media_links("facebook")
    assert "https://www.facebook.com/saucelabs" in logged_in_driver.current_url, "page navigation is wrong"

    inventory.validate_social_media_links("linkedin")
    assert "https://www.linkedin.com/company/sauce-labs/" in logged_in_driver.current_url, "page navigation is wrong"


    inventory.get_menu_options()
    assert inventory.is_burger_menu_opened()