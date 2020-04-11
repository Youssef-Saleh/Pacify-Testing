import time
from selenium import webdriver
from pages.home.Login_page import LoginPage
import unittest
class LoginTest(unittest.TestCase):

    def test_validlogin(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.stress_login1()
        # lp.stress_login2()
        # lp.stress_login3()
        # lp.stress_login4()
        lp.stress_login5()