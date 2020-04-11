from selenium.webdriver.common.by import By


class SearchPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._SearchLink = "Search"

    def getSearchLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._SearchLink)

    def clickSearchLink(self):
        self.getSearchLink().click()

    def LoadSearchPage(self):
        self.clickSearchLink()

    def verifySearchPageLoaded(self):
        try:
            YourTopGenres = self.driver.find_element(By.XPATH, "//h1[contains(.,'Your top genres')]")
            BrowseAll = self.driver.find_element(By.XPATH, "//h1[contains(.,'Browse all')]")
            return True
        except:
            return False
