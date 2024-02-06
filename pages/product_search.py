import time

from utils.utilities import is_increasing
from locators.locators import ProductSearchLocators
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import allure

class ProductSearch:

    def __init__(self, driver):
        # Initialize the ProductSearch object
        self.driver = driver
        # Assign locators to variables
        self.search_input_xpath = ProductSearchLocators.search_input_xpath
        self.search_result_check_css = ProductSearchLocators.search_result_check_css
        self.dropdown_tag_name = ProductSearchLocators.dropdown_tag_name
        self.search_order_page = ProductSearchLocators.search_order_page

    @allure.step("Input product '{1}")
    def search_product(self, search_query):
        # Find the search input field using XPATH
        search_input = self.driver.find_element(By.XPATH, self.search_input_xpath)

        # Input the search query and press RETURN
        search_input.send_keys(search_query)
        search_input.send_keys(Keys.RETURN)

    @allure.step("Return the text of the search result")
    def search_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.search_result_check_css).text

    @allure.step("Select the dropdown by tag name and choose")
    def ordering_check(self, search_query):

        self.driver.get(self.search_order_page + search_query)

        # Extract and convert low and high prices
        price_content = self.driver.find_elements(By.CSS_SELECTOR, "div.row:nth-child(3)")
        return is_increasing(price_content)

