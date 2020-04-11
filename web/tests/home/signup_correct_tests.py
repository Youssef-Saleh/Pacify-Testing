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


class Test_C_SignupCorrect(unittest.TestCase, SeleniumDriver):
    # @pytest.fixture(autouse=True)
    # def signupSetup(self, oneTime_signup_SetUp):
    wdf = WebDriverFactory("chrome")
    Driver = wdf.GetWebDriverInstance()
    su = signuppage(Driver)
    ts = TestStatus(Driver)
    su.ClickSignupLink()


    def test_A_BlankEmailSignup(self):
        self.su.Signup(" ", "modyseka@gmail.com", "2222222222", "sayed","09252010",  "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_BlankEmailSignup", result, "Invalid Signup Blank Email")


    def test_B_BlankConfirmEmailSignup(self):
        self.su.Signup("modyseka@gmail.com", " ", "2222222222", "sayed","09252010",  "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_BlankConfirmEmailSignup", result, "Invalid Signup Blank Confirm Email")


    def test_C_BlankDisplaySignup(self):
        self.su.Signup("modyseka@gmail.com", "modyseka@gmail.com", " ", "sayed","09252010","male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_BlankDisplaySignup", result, "Invalid Signup Blank Display")

    def test_D_BlankGenderSignup(self):
        self.su.Signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed","09252010",  " ")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_BlankGenderSignup", result, "Invalid Signup Blank Gender")

    def test_E_InvalidPasswordSignup(self):
        self.su.Signup("modyseka@gmail.com", "modyseka@gmail.com", "222", "sayed", "09252010", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_InvalidPasswordSignup", result, "Invalid Signup Invalid password")

    def test_F_IllegalDateSignup(self):
        self.su.Signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed","09252015",  "female")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_IllegalDateSignup", result, "Invalid Signup")

    def test_G_ValidSignup(self):
        # we should put new email that is not exist in the database
        self.su.Signup("okay113@gmail.com", "okay113@gmail.com", "2222222222", "sayed","09252010",  "male")
        time.sleep(2)
        # we should change it after th integration with the other teams
        result = self.su.VerifyLoginSuccessful()
        self.ts.markFinal("test_ValidSignup", result, "sign up done successsfly")
        # self.su.LogoutFN()
        self.Driver.quit()
    ###################################################

