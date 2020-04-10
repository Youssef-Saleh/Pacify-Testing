from selenium import webdriver
from web.pages.home.Home_page import homepage
from web.pages.home.signup_page import signuppage
from web.pages.home.signup_page_f import signuppage_f
import time
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
import unittest

class Test_stress(unittest.TestCase, SeleniumDriver):
    wdf=WebDriverFactory("chrome")
    driver=wdf.getWebDriverInstance()
    hp=homepage(driver)
    suf=signuppage_f(driver)
    su=signuppage(driver)

    def test_stress_a(self):
        for x in range(1000):
            self.hp.click_spotify_logo()
        for x in range(1000):
            self.hp.click_help_link()
            self.hp.click_spotify_logo()
        for x in range(1000):
            self.hp.click_spotify_logo()
            self.hp.click_help_link()
            self.hp.click_premieum_tab()
    def test_stress_b(self):
        self.hp.click_signup_tab()
        for x in range(1000):
            self.su.click_signup_btn()
        for x in range(1000):
            self.suf.click_signup_facebook()
        for x in range(1000):
            self.suf.click_signup_facebook()
            self.su.click_signup_btn()


