from web.base.webdriverfactory import WebDriverFactory
from web.pages.home.signup_page import signuppage
from web.pages.HomePage.Home_page import homepage
from web.base.selenium_driver import SeleniumDriver
from web.utilities.teststatues import TestStatus
import unittest
import time


class Test_E_SignupFix(unittest.TestCase, SeleniumDriver):
    # @pytest.fixture(autouse=True)
    # def signupSetup(self, oneTime_signup_SetUp):
    wdf = WebDriverFactory("chrome")
    Driver = wdf.GetWebDriverInstance()
    su = signuppage(Driver)
    hp=homepage(Driver)
    ts = TestStatus(Driver)
    su.ClickSignupLink()

    def test_fixing_Signup(self):
        # we should put new email that is not exist in the database
        self.su.Signup("okay20@gmail.com", "okay20@gmail.com", "2222222222", "sayed","09252010",  "male")
        # we should change it after th integration with the other teams
        result = self.su.VerifyLoginSuccessful()
        self.ts.markFinal("test_ValidSignup", result, "sign up done successsfly")
        # self.su.LogoutFN()
        time.sleep(4)
        self.Driver.back()
        self.su.LoginFN("okay20@gmail.com","2222222222")
        result = self.su.VerifyLoginSuccessful()
        self.ts.markFinal("Login after Signup", result, "Login done successsfly")
        self.Driver.quit()