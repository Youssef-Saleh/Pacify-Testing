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
        time.sleep(1)
        lp.Homelogin("","789456123")
        lp.login("modyseka@gamil.com","")
        time.sleep(2)
        lp.login("","")
        time.sleep(2)
        lp.login("modyseka@gamil.com", "abc")
        time.sleep(2)
        lp.login("ahmed@gmail.com", "789456123")
        time.sleep(2)
        lp.login("ahmed.gaber42@yahoo.com", "789456123")
        time.sleep(2)
        lp.login("ahmed", "789456123")
        time.sleep(2)
        lp.login(
            "modyseka@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm",
            "3333333333")
        time.sleep(2)
        lp.login("modyseka@gmail.com",
                 "333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333")
        time.sleep(2)
        lp.login("modyseka@@gmail.com", "789456123")
        time.sleep(2)
        lp.login("modyseka@gmail.", "789456123")
        time.sleep(2)
        lp.login("modyseka.com", "789456123")
        time.sleep(2)
        lp.login("@gmail.com", "789456123")
        time.sleep(2)
        lp.login("modyseka@gmail.com", "789456123")
        lp.loginwithoutremember("789456123")
        lp.login_facebook("01033811138", "ahmedgaber")
        lp.forgetpassword("abc")



