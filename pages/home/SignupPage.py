from selenium.webdriver.common.by import By


class SignupPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._SignupLink = "Sign-up"

    def getSignupLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._SignupLink)

    def clickSignupLink(self):
        self.getSignupLink().click()

    def LoadSignupPage(self):
        self.clickSignupLink()

    def verifySignupPageLoaded(self):
        SignupButton = None
        try:
            SignupButton = self.driver.find_element(By.CSS_SELECTOR, ".SignUp_button_Signup")
            return SignupButton
        except:
            return SignupButton
