from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def pin(self):
        try:
            pin = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'number')]"))
            )
            assert pin.is_displayed(), "pin input is not displayed on the page."
            pin.send_keys(2982)

        except Exception as e:
            print(f"Assertion failed: {e}")


    def LoginButton(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//input[contains(@type,'submit')])[1]"))
            )
            assert button.is_displayed(), "button input is not displayed on the page."
            button.click()

        except Exception as e:
            print(f"Assertion failed: {e}")
