import allure
from pages.product_search import ProductSearch
from constans.constants import Constants
from tests.conftest import setup
import pytest


# Using the "setup" fixture for setup before the test
@pytest.mark.usefixtures("setup")
class TestPositiveSearch:

    @allure.title("Testing correct product search")
    @pytest.mark.parametrize("search_query", Constants.VALID_SEARCH_DATA)
    def test_search_for_a_valid_product(self, search_query):
        # Initialize the product search page
        product_search = ProductSearch(self.driver)

        # Search for a product using the provided query
        product_search.search_product(search_query)

        # Get text from the search results
        result = product_search.search_result()

        # Check if the query is present in the results
        assert search_query in result, f"Expected '{search_query}' in search results, got '{result}'"
