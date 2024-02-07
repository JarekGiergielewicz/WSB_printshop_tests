import allure
from tests.conftest import setup
from pages.login_page import LoginPage
from constans.constants import Constants
import pytest

# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestInvalidLogin:

    @pytest.mark.parametrize("email, password", Constants.FAILED_LOGIN_DATA)
    @allure.title("Testing login with invalid data")
    def test_log_invalid(self, email, password):

        # Initialize the login page
        login_pass = LoginPage(self.driver)
        login_pass.disable_cookies()
        login_pass.go_to_login_page()

        # Enter invalid login data
        login_pass.log_in(email, password)
        login_pass.log_in_exe()

        # Check if the error message is as expected
        actual_msg = login_pass.popup_error_msg()
        expected_msg = Constants.popup_error_msg
        assert expected_msg in actual_msg, f"Expected error message: '{expected_msg}', Got: '{actual_msg}'"
