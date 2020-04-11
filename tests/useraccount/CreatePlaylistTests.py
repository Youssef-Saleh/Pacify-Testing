from selenium import webdriver
from pages.useraccount.CreatePlaylistPage import CreatePlaylistPage
import unittest


class CreatePlaylistTests(unittest.TestCase):
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

    def test_LoadCreatePlaylistPage(self):
        driver = self.driver
        CP = CreatePlaylistPage(driver)

        CP.LoadCreatePlaylistPage()
        CreatePlaylistPageLoaded = CP.verifyCreatePlaylistPageLoaded()
        self.assertTrue(CreatePlaylistPageLoaded, msg="CreatePlaylist Page not loaded")

    def test_CancelCreatePlaylistPage(self):
        driver = self.driver
        CP = CreatePlaylistPage(driver)

        CP.LoadCreatePlaylistPage()
        CP.clickCancelButtonCSS()
        CreatePlaylistPageCanceled = CP.verifyCancelButtonClicked()
        self.assertTrue(CreatePlaylistPageCanceled, msg="Create Playlist Page not canceled")

    def test_CloseCreatePlaylistPage(self):
        driver = self.driver
        CP = CreatePlaylistPage(driver)

        CP.LoadCreatePlaylistPage()
        CP.clickCloseButtonCSS()
        CreatePlaylistPageClosed = CP.verifyCloseButtonClicked()
        self.assertTrue(CreatePlaylistPageClosed, msg="Create Playlist Page not closed")

    def tearDown(self):
        self.driver.quit()
