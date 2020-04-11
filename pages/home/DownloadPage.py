from selenium.webdriver.common.by import By


class DownloadPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._DownloadLink = "Download"

    def getDownloadLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._DownloadLink)

    def clickDownloadLink(self):
        self.getDownloadLink().click()

    def LoadDownloadPage(self):
        self.clickDownloadLink()

    def verifyDownloadPageLoaded(self):
        LaptopImage = None
        try:
            LaptopImage = self.driver.find_element(By.ID, "laptop")
            return LaptopImage
        except:
            return LaptopImage
