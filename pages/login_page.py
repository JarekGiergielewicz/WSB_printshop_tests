from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from locators.locators import LoginPageLocators
from utils.utilities import wait_for_element
import allure

class LoginPage:

    def __init__(self, driver):
        # Initialize the LoginPage object
        self.driver = driver
        # Assign locators to variables
        self.log_in_menu_xpath = LoginPageLocators.log_in_menu_xpath
        self.to_login_page_link_text = LoginPageLocators.to_login_page_link_text
        self.email_input_css = LoginPageLocators.email_input_css
        self.password_input_css = LoginPageLocators.password_input_css
        self.button_css = LoginPageLocators.button_css
        self.error_msg_popup_css = LoginPageLocators.error_msg_popup_css
        self.popup_close__css = LoginPageLocators.popup_close__css
        self.blank_error_css = LoginPageLocators.blank_error_css
        self.log_off_menu_xpath = LoginPageLocators.log_off_menu_xpath
        self.logoff_check_link_text = LoginPageLocators.logoff_check_link_text

    @allure.step("Go to the login page")
    def go_to_login_page(self):
        # Click the login button in the menu
        self.driver.find_element(By.XPATH, self.log_in_menu_xpath).click()

        # Click the link leading to the login page
        wait_for_element(self.driver, By.LINK_TEXT, self.to_login_page_link_text).click()

    @allure.step("Log off check")
    def log_off_check(self):
        # Click the log off button in the menu
        self.driver.find_element(By.XPATH, self.log_off_menu_xpath).click()
        # Click the link checking the log off
        self.driver.find_element(By.LINK_TEXT, self.logoff_check_link_text).click()
        # Return the text from the login button
        return self.driver.find_element(By.XPATH, self.log_in_menu_xpath).text

    @allure.step("Find the email field, clear it, and enter the given email '{1}'")
    def enter_email(self, email):
        user_mail = self.driver.find_element(By.CSS_SELECTOR, self.email_input_css)
        user_mail.clear()
        user_mail.send_keys(email)
        user_mail.send_keys(Keys.ENTER)

    @allure.step("Find the password field, clear it, and enter the given password '{1}'")
    def enter_password(self, password):
        user_password = self.driver.find_element(By.CSS_SELECTOR, self.password_input_css)
        user_password.clear()
        user_password.send_keys(password)
        user_password.send_keys(Keys.ENTER)

    @allure.step("Invoke methods to input email '{1}' and password '{2}'")
    def log_in(self, email, password):
        self.enter_email(email)
        self.enter_password(password)

    @allure.step("Click the login button")
    def log_in_exe(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_css).click()

    @allure.step("Return the text from the log off button")
    def log_in_check(self):
        return self.driver.find_element(By.XPATH, self.log_off_menu_xpath).text

    @allure.step("Click the close button on the popup window")
    def popup_close(self):
        self.driver.find_element(By.CSS_SELECTOR, self.popup_close__css).click()

    @allure.step("Check if the alert is active")
    def alert_enable(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.blank_error_css).is_enabled()

    @allure.step("Return the text from the error popup window")
    def popup_error_msg(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.error_msg_popup_css).text
