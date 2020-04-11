from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        # Locators
        self._LoginLink = "Login"

    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._LoginLink)

    def clickLoginLink(self):
        self.getLoginLink().click()

    def LoadLoginPage(self):
        self.clickLoginLink()

    def verifyLoginPageLoaded(self):
        LoginButton = None
        try:
            LoginButton = self.driver.find_element(By.CSS_SELECTOR, ".Login_button_login")
            return LoginButton
        except:
            return LoginButton
