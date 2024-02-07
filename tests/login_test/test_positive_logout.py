from pages.login_page import LoginPage
from constans.constants import Constants
from tests.conftest import setup
import pytest
import allure


# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestPositiveLogout:

    @pytest.mark.parametrize("email, password", Constants.VALID_LOGIN_DATA)
    @allure.title("Testing positive logout")
    def test_log_out_pass(self, email, password):

        # Initialize the login page
        login_pass = LoginPage(self.driver)
        login_pass.disable_cookies()
        login_pass.go_to_login_page()

        # Log in with valid credentials
        login_pass.log_in(email, password)
        login_pass.log_in_exe()

        # Check if the logout was successful
        assert login_pass.log_off_check() == Constants.logout_msg, f"Expected logout message: '{Constants.logout_msg}', Got: '{login_pass.log_off_check()}'"
