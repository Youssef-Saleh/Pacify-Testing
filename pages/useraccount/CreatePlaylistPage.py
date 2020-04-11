from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CreatePlaylistPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._CreatePlaylistXPATH = "//span[contains(.,'Create Playlist')]"
        self._CreateButtonCSS = ".create-button > .create"
        self._CancelButtonCSS = ".Cancel"
        self._CloseButtonCSS = "path:nth-child(2)"

    def getCreatePlaylistLink(self):
        return self.driver.find_element(By.XPATH, self._CreatePlaylistXPATH)

    def clickCreatePlaylistLink(self):
        self.getCreatePlaylistLink().click()

    def LoadCreatePlaylistPage(self):
        self.clickCreatePlaylistLink()

    def verifyCreatePlaylistPageLoaded(self):
        try:
            CreatePlaylist = self.driver.find_element(By.XPATH, "//h1[contains(.,'Create a new playlist')]")
            return True
        except:
            return False

    def getCancelButtonCSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._CancelButtonCSS)

    def clickCancelButtonCSS(self):
        self.getCancelButtonCSS().click()

    def verifyCancelButtonClicked(self):
        try:
            WebDriverWait(self.driver, 30000).until(expected_conditions.invisibility_of_element_located(
                (By.XPATH, "//h1[contains(.,\'Create a new playlist\')]")))
            CreatePlaylist = self.driver.find_element(By.XPATH, "//h1[contains(.,'Create a new playlist')]")
            return False
        except:
            return True

    def getCloseButtonCSS(self):
        return self.driver.find_element(By.CSS_SELECTOR, self._CloseButtonCSS)

    def clickCloseButtonCSS(self):
        self.getCloseButtonCSS().click()

    def verifyCloseButtonClicked(self):
        try:
            WebDriverWait(self.driver, 30000).until(expected_conditions.invisibility_of_element_located(
                (By.XPATH, "//h1[contains(.,\'Create a new playlist\')]")))
            CreatePlaylist = self.driver.find_element(By.XPATH, "//h1[contains(.,'Create a new playlist')]")
            return False
        except:
            return True
