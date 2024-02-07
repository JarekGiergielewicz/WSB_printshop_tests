from constans.constants import Constants
from pages.login_page import LoginPage
from tests.conftest import setup
import pytest
import allure

# Preliminary settings for the tests
@pytest.mark.usefixtures("setup")
class TestPositiveLogin:

    @allure.title("Testing positive login with test data")
    @pytest.mark.parametrize("email, password", Constants.VALID_LOGIN_DATA)
    def test_log_in_pass(self, email, password):

        # Initialize the login page
        login_pass = LoginPage(self.driver)
        login_pass.disable_cookies()
        login_pass.go_to_login_page()

        # Log in with test data
        login_pass.log_in(email, password)
        login_pass.log_in_exe()

        # Check if the login was successful
        actual_msg = login_pass.log_in_check()
        expected_msg = Constants.log_in_check_msg
        assert actual_msg == expected_msg, f"Expected: '{expected_msg}', Received: '{actual_msg}'"
