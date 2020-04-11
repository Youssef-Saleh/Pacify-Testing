from selenium.webdriver.common.by import By


class LibraryPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._LibraryLink = "Library"
        self._PlaylistsLink = "Playlists"
        self._AlbumsLink = "Albums"

    def getLibraryLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._LibraryLink)

    def clickLibraryLink(self):
        self.getLibraryLink().click()

    def LoadLibraryPage(self):
        self.clickLibraryLink()

    def verifyLibraryPageLoaded(self):
        try:
            Playlists = self.driver.find_element(By.XPATH, "//h1[contains(.,'Playlists')]")
            return True
        except:
            return False

    def getPlaylistsLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._PlaylistsLink)

    def clickPlaylistsLink(self):
        self.getPlaylistsLink().click()

    def LoadPlaylistsPage(self):
        self.LoadLibraryPage()
        self.clickPlaylistsLink()

    def verifyPlaylistsPageLoaded(self):
        try:
            Playlists = self.driver.find_element(By.XPATH, "//h1[contains(.,'Playlists')]")
            return True
        except:
            return False

    def getAlbumsLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._AlbumsLink)

    def clickAlbumsLink(self):
        self.getAlbumsLink().click()

    def LoadAlbumsPage(self):
        self.LoadLibraryPage()
        self.clickAlbumsLink()

    def verifyAlbumsPageLoaded(self):
        try:
            Albums = self.driver.find_element(By.XPATH, "//h1[contains(.,'Albums')]")
            return True
        except:
            return False
