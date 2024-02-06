from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def wait_for_element(driver, by, value, timeout=20):
    # Wait for an element to be visible on the webpage.

    element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    # element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
    return element

def move_to_elenent(element):
    # Scroll to the specified element on the webpage.
    element.location_once_scrolled_into_view


def is_increasing(price_content):
    if len(price_content) == 0:
        return False
    else:
        li_texts = [element.text for element in price_content]

        li_data = str(li_texts)

        data_data = li_data.split("zł")

        # print(data_data)

        content = []
        for i in range(len(data_data)- 1):
            if "PROMOCJA" not in data_data[i]:
                x = data_data[i].split("n")
                y = x[-1].replace(",", ".")
                content.append(float(y))

        if content == sorted(content):
            return True
        else:
            return False