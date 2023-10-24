import time

from selenium import webdriver

from Src.Pages.CartPage import Cartpage
from Src.Pages.LandingPage import LandingPage
from Src.Pages.LoginPage import LoginPage
from Src.Pages.OrderPage import Orderpage
from Src.Pages.ProductPage import ProductPage
from Src.Pages.RegPage import RegPage

driver = webdriver.Chrome()
driver.get('http://shop.icraftsoft.net:8095/')
driver.maximize_window()


# Landing Page
lp = LandingPage(driver)  # object create
time.sleep(2)
lp.click_login()
time.sleep(2)

# Register username and password
rg = RegPage(driver)
rg.getUsername()
time.sleep(2)
rg.getEmail()
time.sleep(2)
rg.getButton()
time.sleep(2)
rg.LogButton()
time.sleep(2)

# Login with pin
Lp = LoginPage(driver)
Lp.pin()
time.sleep(1)
Lp.LoginButton()
time.sleep(4)

# Product page
PP = ProductPage(driver)
PP.Quickview()
time.sleep(3)
PP.FZA()
time.sleep(3)
PP.Quickview1()
time.sleep(3)
PP.Dell()
time.sleep(3)
PP.Cart()
time.sleep(3)

# Cart page
Cp = Cartpage(driver)
Cp.remove()
time.sleep(5)


# Order page
Op = Orderpage(driver)
Op.Buy()
time.sleep(5)










