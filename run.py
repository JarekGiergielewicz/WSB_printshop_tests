import pytest
import os

from utils.driver_factory import DriverFactory


# Run tests with Allure
def run_allure_tests():
    # Execute tests with Allure
    os.system("pytest --alluredir=reports")

    # Generate Allure report
    os.system("allure serve reports")
    os.system("")


if __name__ == "__main__":
    # Run Allure tests an choose driver chrome /firefox
    run_allure_tests()
