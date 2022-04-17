from selenium import webdriver
import time
import unittest
from selenium.webdriver.chrome.service import Service
from POM.Pages.signIn import SignIn
from POM.Pages.dress import CasualDress
from POM.Pages.tShirt import TShirt
from POM.Pages.checkOut import CheckOut
from POM.Pages.signOut import SignOut

class User1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        s = Service("C:\Program Files\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_use1(self):
        driver=self.driver
        driver.get("http://automationpractice.com/index.php")

        login=SignIn(driver)
        login.click_signIn()
        login.enter_email(email="sho@gmail.com")
        driver.implicitly_wait(5)
        login.enter_password(password="12345")
        driver.implicitly_wait(5)
        login.click_logIn()

        dress=CasualDress(driver)
        dress.click_dress()
        driver.implicitly_wait(5)
        dress.click_casual()
        driver.implicitly_wait(5)
        dress.click_product()
        driver.implicitly_wait(5)
        dress.click_cart()
        driver.implicitly_wait(5)
        dress.click_cross()

        shirt=TShirt(driver)
        shirt.click_tShirt()
        driver.implicitly_wait(5)
        shirt.click_blueColor()
        driver.implicitly_wait(5)
        shirt.click_product()
        driver.implicitly_wait(5)
        shirt.click_cart()
        driver.implicitly_wait(5)
        shirt.click_cross()


        pay=CheckOut(driver)
        pay.click_shoppingCart()
        driver.implicitly_wait(5)
        pay.click_proceedCheckOut()
        driver.implicitly_wait(5)
        pay.click_proceedAddress()
        driver.implicitly_wait(5)
        pay.click_checkbox()
        driver.implicitly_wait(5)
        pay.click_proceedShipping()
        driver.implicitly_wait(5)
        pay.click_payByCheck()

        signOut = SignOut(driver)
        signOut.click_signOut()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls) :
        cls.driver.close()
        print("test completed for User1")
