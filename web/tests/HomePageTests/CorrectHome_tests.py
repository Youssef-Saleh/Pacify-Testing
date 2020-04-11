from web.pages.HomePage.Home_page import homepage
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
import time
import unittest

class Test_A_HomeCorrect(unittest.TestCase, SeleniumDriver):

    wdf = WebDriverFactory("Chrome")
    Driver = wdf.GetWebDriverInstance()
    su = homepage(Driver)
    def test_end_login(self):
        self.su.ClickSignupLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickHelpLink()
        self.Driver.forward()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickPremieumLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickDownloadLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickSignupLink()
        time.sleep(1)
        self.Driver.back()
        self.su.clickLoginLink()
        self.Driver.back()


    def test_end_signup(self):
        self.su.ClickHelpLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickPremieumLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickDownloadLink()
        time.sleep(1)
        self.Driver.back()
        self.su.clickLoginLink()
        time.sleep(1)
        self.Driver.back()
        self.su.ClickSignupLink()
        self.Driver.quit()