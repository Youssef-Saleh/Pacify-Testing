from selenium import webdriver
from web.pages.home.Home_page import homepage
from web.tests import conftest
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
from web.utilities.teststatues import TestStatus
import time
import unittest
import pytest

class Test_home(unittest.TestCase,SeleniumDriver):

    wdf = WebDriverFactory("chrome")
    driver = wdf.getWebDriverInstance()
    su = homepage(driver)

    def test_end_login(self):
        self.su.click_signup_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_help_link()
        self.driver.forward()
        time.sleep(1)
        self.driver.back()
        self.su.click_premieum_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_download_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_signup_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_footer_functions(self.driver)
        self.su.click_Login_tab()
        self.driver.back()


    def test_end_signup(self):
        self.su.click_help_link()
        time.sleep(1)
        self.driver.back()
        self.su.click_footer_functions(self.driver)
        self.su.click_premieum_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_download_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_Login_tab()
        time.sleep(1)
        self.driver.back()
        self.su.click_signup_tab()
        self.driver.quit()



