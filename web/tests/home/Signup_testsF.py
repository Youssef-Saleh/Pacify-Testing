from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.webdriverfactory import WebDriverFactory
from web.pages.home.signup_page import signuppage
from web.pages.home.signup_page_f import signuppage_f
from web.tests import conftest
from web.base.selenium_driver import SeleniumDriver
from web.utilities.teststatues import TestStatus
import time
import unittest

class Test_D_SignupCorrectFacebook(unittest.TestCase, SeleniumDriver):
    wdf = WebDriverFactory("chrome")
    Driver = wdf.GetWebDriverInstance()
    su = signuppage(Driver)
    ts = TestStatus(Driver)
    su.ClickSignupLink()

    def test_Facebook(self):
        self.fsu = signuppage_f(self.Driver)
        self.fsu.ClickFacebook()
        ParentHandle = self.Driver.current_window_handle
        Handles = self.Driver.window_handles
        self.fsu.SwitchhandlesLogin(ParentHandle, Handles, self.Driver, "01150297934", "0103098875")
        self.Driver.switch_to.window(ParentHandle)
        time.sleep(5)
        self.Driver.quit()
        #self.fsu.LogoutFN()
        '''result = self.su.VerifyLoginSuccessful()
        self.ts.markFinal("test_ZFacebook", result, "sign up done successsfly")
        self.Driver.quit()'''