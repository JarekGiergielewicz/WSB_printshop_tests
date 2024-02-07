import allure
import pytest
from pages.product_search import ProductSearch
from constans.constants import Constants
from tests.conftest import setup

# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestOrderSearch:

    @allure.title("Testing correct ordering of product search results by price")
    @pytest.mark.parametrize("search_query", Constants.VALID_SEARCH_DATA)
    def test_search_product_correct(self, search_query):
        # Initialize the product search page
        product_search = ProductSearch(self.driver)
        product_search.disable_cookies()

        # Search for a product using the given query
        # product_search.ordering_check(search_query)

        # Check if the search results ordering is correct
        assert product_search.ordering_check(search_query) == True, "Ordering check failed, expected order not found"
