import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.locators import LoginPageLocators
from locators.locators import UserAccountLocators
from constans.constants import Constants
from utils.utilities import wait_for_element
from utils.utilities import move_to_elenent


class UserAccount:

    def __init__(self, driver):
        # Initialize the UserAccount object with driver and locators
        self.driver = driver
        self.log_off_menu_xpath = LoginPageLocators.log_off_menu_xpath
        self.accountlink_link_text = UserAccountLocators.accountlink_link_text
        self.edit_account_link_text = UserAccountLocators.edit_account_link_text
        self.user_firstname_css = UserAccountLocators.user_firstname_css
        self.user_lastname_css = UserAccountLocators.user_lastname_css
        self.user_phone_css = UserAccountLocators.user_phone_css
        self.dropbox_menu_xpath = UserAccountLocators.dropbox_menu_xpath
        self.textbox_css = UserAccountLocators.textbox_css
        self.user_city_css = UserAccountLocators.user_city_css
        self.user_street_css = UserAccountLocators.user_street_css
        self.user_code_css = UserAccountLocators.user_code_css
        self.submit_button_css = UserAccountLocators.submit_button_css
        self.phone_check_xpath = UserAccountLocators.phone_check_xpath
        self.name_check_xpath = UserAccountLocators.name_check_xpath
        self.adress_check_xpath = UserAccountLocators.adress_check_xpath
        self.cookie_css = LoginPageLocators.cookie_css



    @allure.step("Go to account page")
    def go_to_account(self):
        # Navigate to the account page
        self.driver.find_element(By.XPATH, self.log_off_menu_xpath).click()
        self.driver.find_element(By.LINK_TEXT, self.accountlink_link_text).click()
        self.driver.find_element(By.LINK_TEXT, self.edit_account_link_text).click()

    @allure.step("Edit account data")
    def account_edit(self):
        # Edit account data

        self.driver.find_element(By.CSS_SELECTOR, self.user_firstname_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_firstname_css).send_keys(Constants.FNAME)

        self.driver.find_element(By.CSS_SELECTOR, self.user_lastname_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_lastname_css).send_keys(Constants.LNAME)

        self.driver.find_element(By.CSS_SELECTOR, self.user_phone_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_phone_css).send_keys(Constants.PHONE_NUMBER)

        self.driver.find_element(By.XPATH, self.dropbox_menu_xpath).click()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_css).send_keys(Constants.COUNTRY)
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_css).send_keys(Keys.ENTER)

        self.driver.find_element(By.CSS_SELECTOR, self.user_city_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_city_css).send_keys(Constants.CITY)

        self.driver.find_element(By.CSS_SELECTOR,self.user_street_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_street_css).send_keys(Constants.STREET)

        self.driver.find_element(By.CSS_SELECTOR, self.user_code_css).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.user_code_css).send_keys(Constants.CODE)

        move_to_elenent(self.driver.find_element(By.CSS_SELECTOR, self.submit_button_css))
        self.driver.find_element(By.CSS_SELECTOR, self.submit_button_css).click()

    @allure.step("Function to disable cookies on the website.")
    def disable_cookies(self):
        self.driver.find_element(By.CSS_SELECTOR, self.cookie_css).click()

    @allure.step("Account data check")
    def account_data_check(self):
        # Check account data

        wait_for_element(self.driver, By.XPATH, self.log_off_menu_xpath).click()

        self.driver.find_element(By.LINK_TEXT, self.accountlink_link_text).click()

        phone_check = self.driver.find_element(By.XPATH, self.phone_check_xpath).text
        name_check = self.driver.find_element(By.XPATH, self.name_check_xpath).text
        adress_check = self.driver.find_element(By.XPATH, self.adress_check_xpath).text

        return phone_check[:-2], name_check[:-2], adress_check[0:-2]


