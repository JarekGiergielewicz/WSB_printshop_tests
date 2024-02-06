import allure
from pages.login_page import LoginPage
from constans.constants import Constants
from tests.conftest import setup
import pytest

# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestEmptyLogin:

    @pytest.mark.parametrize("email, password", Constants.BLANK_LOGIN_DATA)
    @allure.title("Testing login with empty data")
    def test_empty_data_login(self, email, password):

        # Initialize the login page
        login_pass = LoginPage(self.driver)
        login_pass.go_to_login_page()

        # Enter empty login data
        login_pass.log_in(email, password)

        # Check if the alert for empty login data is active
        assert login_pass.alert_enable() == True, "Alert for empty login data is not displayed"

