from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


class DriverFactory:

    @staticmethod
    def create_driver(browser_name='chrome'):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        elif browser_name.lower() == 'firefox':
            # return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=option)
            return webdriver.Firefox()

        else:
            raise ValueError("Unsupported browser. Please choose 'chrome' or 'firefox'.")
