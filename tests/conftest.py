import allure
from selenium import webdriver
import pytest
import allure
from utils.driver_factory import DriverFactory


@pytest.fixture()
def setup(request):
    # global driver
    driver = DriverFactory.create_driver("firefox")
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    driver.get("https://printshop-24.pl")
    before_failed = request.session.testsfailed
    print(before_failed)

    yield
    if request.session.testsfailed != before_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Test failed",
            attachment_type=allure.attachment_type.PNG)
    driver.quit()