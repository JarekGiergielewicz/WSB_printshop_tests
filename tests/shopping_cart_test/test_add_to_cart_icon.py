from pages.shopping_cart_page import CartPage
from tests.conftest import setup
import pytest
import allure


# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestShoppingIcon:

    @allure.title("Testing shopping basket icon")
    def test_add_to_cart_basket_icon(self):
        # Initialize the CartPage object
        cart_page = CartPage(self.driver)

        # Steps 1 and 2: Select a product and perform operations on the basket
        cart_page.choose_product()
        cart_page.basket_operations()

        # Check the number of products in the basket icon
        assert cart_page.basket_icon_check() == "2"
