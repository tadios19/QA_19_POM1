from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select



class ProductPage:
    def __init__(self, driver):  # constructor method
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def Quickview(self):
        try:
            product = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[@type='button'][contains(.,'Quick View')])[1]"))
            )
            product.click()
            # Locate the dropdown element
            dropdown = Select(self.driver.find_element(By.XPATH, "(//select[contains(@class,'form-control')])[2]"))

            # Select an option by its visible text
            dropdown.select_by_visible_text("2")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def FZA(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'][contains(.,'Add to cart')])[31]"))
            )
            cart.click()
            assert cart.is_displayed(), "cart button is not displayed on the page."


        except Exception as e:
            print(f"Assertion failed: {e}")

    def Quickview1(self):
        try:
            product = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[@type='button'][contains(.,'Quick View')])[2]"))
            )
            product.click()
            # Locate the dropdown element
            dropdown = Select(self.driver.find_element(By.XPATH, "(//select[contains(@class,'form-control')])[3]"))

            # Select an option by its visible text
            dropdown.select_by_visible_text("3")

        except Exception as e:
            print(f"Assertion failed: {e}")

    def Dell(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[@type='submit'][contains(.,'Add to cart')])[32]"))
            )
            cart.click()
            assert cart.is_displayed(), "cart button is not displayed on the page."


        except Exception as e:
            print(f"Assertion failed: {e}")

    def Cart(self):
        try:
            cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Cart"))
            )
            assert cart.is_displayed(), "product input is not displayed on the page."
            cart.click()


        except Exception as e:
            print(f"Assertion failed: {e}")


