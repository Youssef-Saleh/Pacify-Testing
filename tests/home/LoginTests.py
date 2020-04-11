from selenium import webdriver
from pages.home.LoginPage import LoginPage
import unittest


class LoginTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)

    def test_LoadLoginPage(self):
        driver = self.driver
        LP = LoginPage(driver)

        LP.LoadLoginPage()
        LoginButton = LP.verifyLoginPageLoaded()
        self.assertIsNotNone(LoginButton, msg="Download Page not loaded")

    def tearDown(self):
        self.driver.quit()
