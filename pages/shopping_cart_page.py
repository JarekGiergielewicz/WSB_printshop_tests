import time
from utils.utilities import move_to_elenent
from selenium.webdriver.common.by import By
from locators.locators import ShoppingCartLocators
import allure

class CartPage:
    def __init__(self, driver):
        # Initialize the CartPage object:
        self.driver = driver
        self.menu_link_text = ShoppingCartLocators.menu_link_text
        self.menu_pillow_xpath = ShoppingCartLocators.menu_pillow_xpath
        self.pillow_content_xpath = ShoppingCartLocators.pillow_content_xpath
        self.increasing_Cart_css = ShoppingCartLocators.increasing_Cart_css
        self.add_to_cart_css = ShoppingCartLocators.add_to_cart_css
        self.click_basket_icon_css = ShoppingCartLocators.click_basket_icon_css
        self.cart_item_quantity_css = ShoppingCartLocators.cart_item_quantity_css
        self.tile_css = ShoppingCartLocators.tile_css
        self.product_css = ShoppingCartLocators.product_css
        self.remove_basket_css = ShoppingCartLocators.remove_basket_css
        self.ok_remove_button_css = ShoppingCartLocators.ok_remove_button_css
        self.remove_info_xpath = ShoppingCartLocators.remove_info_xpath

    @allure.step("Choose product")
    def choose_product(self):
        # Step 1: Go to the menu.
        self.driver.find_element(By.LINK_TEXT, self.menu_link_text).click()

        # Step 2: Choose a product for editing.
        self.driver.find_element(By.XPATH, self.menu_pillow_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, self.pillow_content_xpath).click()

    @allure.step("Increase product quantity in the cart")
    def basket_operations(self):
        # Step 3: Increase the quantity of the product in the cart.
        self.driver.find_element(By.CSS_SELECTOR, self.increasing_Cart_css).click()

        # Step 4: Add the product to the cart.
        self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart_css).click()

        # Refresh the page.
        self.driver.refresh()

    @allure.step("Check basket icon")
    def basket_icon_check(self):
        # Step 5: Check the basket icon.
        self.driver.find_element(By.CSS_SELECTOR, self.click_basket_icon_css).click()

        # Get the quantity of products in the basket.
        cart_quantity = self.driver.find_element(By.CSS_SELECTOR, self.cart_item_quantity_css).text
        return cart_quantity

    @allure.step("Remove products from the cart")
    def remove_product_from_cart(self):
        # Step 1: Click on the tile of the printed mug.
        move_to_elenent(self.driver.find_element(By.CSS_SELECTOR, self.tile_css))
        self.driver.find_element(By.CSS_SELECTOR, self.tile_css).click()

        # Step 2: Click on a specific product.
        self.driver.find_element(By.XPATH, self.product_css).click()


        # Step 3: Click the "Add to Cart" button.
        self.driver.find_element(By.CSS_SELECTOR, self.add_to_cart_css).click()

        # Step 4: Click the basket removal icon.
        self.driver.find_element(By.CSS_SELECTOR, self.remove_basket_css).click()

        # Step 5: Confirm the removal of the product from the cart.
        self.driver.find_element(By.CSS_SELECTOR, self.ok_remove_button_css).click()

        # Return information about the removal of the product.
        return self.driver.find_element(By.XPATH, self.remove_info_xpath).text