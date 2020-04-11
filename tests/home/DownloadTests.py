from selenium import webdriver
from pages.home.DownloadPage import DownloadPage
import unittest


class DownloadTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)

    def test_LoadDownloadPage(self):
        driver = self.driver
        DP = DownloadPage(driver)

        DP.LoadDownloadPage()
        DownloadInstructions = DP.verifyDownloadPageLoaded()
        self.assertIsNotNone(DownloadInstructions, msg="Download Page not loaded")

    def tearDown(self):
        self.driver.quit()
