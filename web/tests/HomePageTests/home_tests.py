from web.pages.HomePage.Home_page import homepage
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
import time
import unittest


class Test_B_Home(unittest.TestCase, SeleniumDriver):

    wdf = WebDriverFactory("Chrome")
    Driver = wdf.GetWebDriverInstance()
    su = homepage(Driver)
    def test_ADownload(self):
        #click And check downlading file
        self.su.ClickDownloadLink()
        self.su.ClickTryAgain()
        time.sleep(1)
        self.Driver.back()
    def test_Bpremium(self):
        time.sleep(1)
        self.su.ClickPremieumLink()
    def test_CSignup(self):
        self.su.ClickSignupLink()
        self.su.ClickTermsandConditions()
        self.su.ClickPrivacy()
        time.sleep(1)
        self.Driver.quit()

    #it makes nothing
    '''def test_ClickFooter(self):
        self.su.ClickFooterFN(self.Driver)'''





