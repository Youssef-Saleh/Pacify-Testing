from selenium.webdriver.common.by import By


class HelpPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._HelpLink = "Help"
        self._WatchButton = ".active .btn"
        self._FirstCarouselItem = ".carousel-indicators > li:nth-child(1)"
        self._SecondCarouselItem = "li:nth-child(2)"
        self._ThirdCarouselItem = "li:nth-child(3)"
        self._FourthCarouselItem = "li:nth-child(4)"
        self._FifthCarouselItem = "li:nth-child(5)"

    def getHelpLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._HelpLink)

    def clickHelpLink(self):
        self.getHelpLink().click()

    def LoadHelpPage(self):
        self.clickHelpLink()

    def verifyHelpPageLoaded(self):
        SearchBar = None
        try:
            SearchBar = self.driver.find_element(By.ID, "search")
            return SearchBar
        except:
            return SearchBar

    def getFirstCarouselItem(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._FirstCarouselItem)

    def clickFirstCarouselItem(self):
        self.getFirstCarouselItem().click()

    def getSecondCarouselItem(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._SecondCarouselItem)

    def clickSecondCarouselItem(self):
        self.getSecondCarouselItem().click()

    def getThirdCarouselItem(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._ThirdCarouselItem)

    def clickThirdCarouselItem(self):
        self.getThirdCarouselItem().click()

    def getFourthCarouselItem(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._FourthCarouselItem)

    def clickFourthCarouselItem(self):
        self.getFourthCarouselItem().click()

    def getFifthCarouselItem(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._FifthCarouselItem)

    def clickFifthCarouselItem(self):
        self.getFifthCarouselItem().click()

    def getWatchButton(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._WatchButton)

    def clickWatchButton(self):
        self.getWatchButton().click()

    def verifyWatchButtonClicked(self):
        Player = None
        try:
            Player = self.driver.find_element(By.ID, "player")
            return Player
        except:
            return Player
