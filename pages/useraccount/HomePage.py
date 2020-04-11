from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._HomeLink = "Home"

    def getHomeLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._HomeLink)

    def clickHomeLink(self):
        self.getHomeLink().click()

    def LoadHomePage(self):
        self.clickHomeLink()

    def verifyHomePageLoaded(self):
        try:
            RecentlyPlayed = self.driver.find_element(By.LINK_TEXT, "Recently Played")
            PopularPlaylists = self.driver.find_element(By.LINK_TEXT, "Popular Playlists")
            PopularAlbums = self.driver.find_element(By.LINK_TEXT, "Popular Albums")
            return True
        except:
            return False
