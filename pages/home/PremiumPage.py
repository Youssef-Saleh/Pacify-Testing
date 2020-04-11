from selenium.webdriver.common.by import By


class PremiumPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._PremiumLink = "Premium"

    def getPremiumLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._PremiumLink)

    def clickPremiumLink(self):
        self.getPremiumLink().click()

    def LoadPremiumPage(self):
        self.clickPremiumLink()

    def verifyPremiumPageLoaded(self):
        PremiumButton = None
        try:
            PremiumButton = self.driver.find_element(By.XPATH, "//button[contains(.,\'GET PREMIUM\')]")
            return PremiumButton
        except:
            return PremiumButton
