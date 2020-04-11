from selenium import webdriver
from pages.home.SignupPage import SignupPage
import unittest


class SignupTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)

    def test_LoadSignupPage(self):
        driver = self.driver
        SP = SignupPage(driver)

        SP.LoadSignupPage()
        SignupButton = SP.verifySignupPageLoaded()
        self.assertIsNotNone(SignupButton, msg="Download Page not loaded")

    def tearDown(self):
        self.driver.quit()
