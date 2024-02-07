import allure
from tests.conftest import setup
from pages.login_page import LoginPage
from pages.user_account import UserAccount
from constans.constants import Constants
import pytest


# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestAccount:

    @pytest.mark.parametrize("email, password", Constants.VALID_LOGIN_DATA)
    @allure.title("Testing the correctness of changing data on the account")
    def test_account(self, email, password):
        # Initialize the login page
        login_page = LoginPage(self.driver)
        login_page.disable_cookies()

        # Go to the login page
        login_page.go_to_login_page()

        # Log in with the provided data
        login_page.log_in(email, password)
        login_page.log_in_exe()

        # Initialize the user account page
        user_account = UserAccount(self.driver)

        # Go to the user account page
        user_account.go_to_account()

        # Edit user account data
        user_account.account_edit()

        # Check if the user account data matches the expected data
        assert user_account.account_data_check() == Constants.ACCOUNT_DATA, "Account data does not match expected data"
