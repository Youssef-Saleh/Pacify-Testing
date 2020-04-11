from selenium import webdriver
from pages.home.PremiumPage import PremiumPage
import unittest


class PremiumTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)

    def test_LoadPremiumPage(self):
        driver = self.driver
        PP = PremiumPage(driver)

        PP.LoadPremiumPage()
        PremiumButton = PP.verifyPremiumPageLoaded()
        self.assertIsNotNone(PremiumButton, msg="Premium Page not loaded")

    def tearDown(self):
        self.driver.quit()
