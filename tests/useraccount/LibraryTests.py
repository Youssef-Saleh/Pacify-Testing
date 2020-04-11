from selenium import webdriver
from pages.useraccount.LibraryPage import LibraryPage
import unittest


class LibraryTests(unittest.TestCase):
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

    def test_LoadLibraryPage(self):
        driver = self.driver
        LP = LibraryPage(driver)

        LP.LoadLibraryPage()
        LibraryPageLoaded = LP.verifyLibraryPageLoaded()
        self.assertTrue(LibraryPageLoaded, msg="Library Page not loaded")

    def test_LoadPlaylistsPage(self):
        driver = self.driver
        LP = LibraryPage(driver)

        LP.LoadPlaylistsPage()
        PlaylistsPageLoaded = LP.verifyPlaylistsPageLoaded()
        self.assertTrue(PlaylistsPageLoaded, msg="Playlists Page not loaded")

    def test_LoadAlbumPage(self):
        driver = self.driver
        LP = LibraryPage(driver)

        LP.LoadAlbumsPage()
        AlbumsPageLoaded = LP.verifyAlbumsPageLoaded()
        self.assertTrue(AlbumsPageLoaded, msg="Albums Page not loaded")

    def tearDown(self):
        self.driver.quit()
