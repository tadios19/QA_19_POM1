from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Cartpage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def remove(self):
        try:
            remove = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "remove "))
            )
            assert remove.is_displayed(), "remove button is not displayed on the page."
            remove.click()


        except Exception as e:
            print(f"Assertion failed: {e}")

    def Cart(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Cart"))
            )
            assert cart.is_displayed(), "cart button is not displayed on the page."
            cart.click()


        except Exception as e:
            print(f"Assertion failed: {e}")