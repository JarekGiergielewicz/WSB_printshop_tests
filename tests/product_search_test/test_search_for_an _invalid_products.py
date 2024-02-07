import allure
from tests.conftest import setup
from pages.product_search import ProductSearch
from constans.constants import Constants
import pytest


# Użycie fixture "setup" do konfiguracji przed testem
@pytest.mark.usefixtures("setup")
class TestNegativeSearch:

    @allure.title("Testing search for an invalid product")
    @pytest.mark.parametrize("search_query", Constants.INVALID_SEARCH_DATA)
    def test_search_for_invalid_product(self, search_query):
        # Initialize the product search page
        product_search = ProductSearch(self.driver)
        product_search.disable_cookies()

        # Search for a product using an invalid query
        product_search.search_product(search_query)

        # Get text from the search results
        result = product_search.search_result()

        # Check if the expected no results message is not present in the results
        assert Constants.search_msg not in result, \
            f"Unexpected '{Constants.search_msg}' found in search results for '{search_query}'"