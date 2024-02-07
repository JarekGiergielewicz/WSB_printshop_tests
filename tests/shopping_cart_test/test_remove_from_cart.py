import allure
import pytest
from tests.conftest import setup
from constans.constants import Constants
from pages.shopping_cart_page import CartPage

# Użycie fixture "setup" do konfiguracji przed testem
@pytest.mark.usefixtures("setup")
class TestRemoveFromCart:

    @allure.title("Remove product from cart")
    def test_remove_product_from_cart(self):
        # Initialize the CartPage object
        cart_page = CartPage(self.driver)
        cart_page.disable_cookies()

        # Step: Remove the product from the cart
        removed_product_msg = cart_page.remove_product_from_cart()

        # Check if the empty cart message is as expected
        assert Constants.empty_basket_msg == removed_product_msg