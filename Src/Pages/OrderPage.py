from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Orderpage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    def Buy(self):
        try:
            Buy = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'submit')])[2]"))
            )
            assert Buy.is_displayed(), "Buy button is not displayed on the page."
            Buy.click()


        except Exception as e:
            print(f"Assertion failed: {e}")