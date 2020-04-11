from selenium import webdriver
from pages.useraccount.SearchPage import SearchPage
import unittest


class SearchTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_css_selector("a:nth-child(5) .white").click()
        self.driver.find_element_by_name("email").click()
        self.driver.find_element_by_name("email").send_keys("editingmaster@artist.pacify")
        self.driver.find_element_by_name("password").send_keys("Dehkmodhek2")
        self.driver.find_element_by_css_selector(".Login_button_login").click()

    def test_LoadSearchPage(self):
        driver = self.driver
        SP = SearchPage(driver)

        SP.LoadSearchPage()
        SearchPageLoaded = SP.verifySearchPageLoaded()
        self.assertTrue(SearchPageLoaded, msg="Search Page not loaded")

    def tearDown(self):
        self.driver.quit()
