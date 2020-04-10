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
import pytest
@pytest.mark.usefixtures("oneTime_signup_SetUp", "signup_setUp")
class Testsignup(unittest.TestCase, SeleniumDriver):
    # @pytest.fixture(autouse=True)
    # def signupSetup(self, oneTime_signup_SetUp):
    wdf = WebDriverFactory("chrome")
    driver = wdf.getWebDriverInstance()
    su = signuppage(driver)
    su.click_signup_link()
    ts = TestStatus(driver)

    @pytest.mark.run(order=1)
    def test_existing_email_signup(self):
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed", "27", 2, "1999", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_existing_email_signup", result, "Invalid Signup")

    @pytest.mark.run(order=2)
    def test_invalid_password_signup(self):
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "22", "sayed", "27", 2, "1999", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_invalid_password_signup", result, "Invalid Signup")

    @pytest.mark.run(order=3)
    def test_blank_email_signup(self):
        self.su.signup("", "modyseka@gmail.com", "2222222222", "", "27", 2, "1999", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_blank_email_signup", result, "Invalid Signup")

    @pytest.mark.run(order=4)
    def test_blank_confirm_email_signup(self):
        self.su.signup("modyseka@gmail.com", "", "2222222222", "sayed", "27", 2, "1999", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_blank_confirm_email_signup", result, "Invalid Signup")

    @pytest.mark.run(order=5)
    def test_blank_display_signup(self):
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "", "sayed", "27", 2, "1999", "male")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_blank_display_signup", result, "Invalid Signup")

    @pytest.mark.run(order=6)
    def test_blank_gender_signup(self):
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed", "27", 2, "1999", "")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_blank_gender_signup", result, "Invalid Signup")

    @pytest.mark.run(order=7)
    def test_illegal_date_signup(self):
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed", "31", 2, "2012", "female")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_illegal_date_signup", result, "Invalid Signup")

    @pytest.mark.run(order=8)
    def test_invalid_email_signup(self):
        self.su.signup("skhfwiod%", "modyseka@gmail.com", "2222222222", "sayed", "31", 2, "2012", "female")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_invalid_email_signup", result, "Invalid Signup")

    @pytest.mark.run(order=9)
    def test_non_equal_email_signup(self):
        self.su.signup("modystery@gmail.com", "hdhksh@gmail.com", "2222222222", "sayed", "31", 2, "2012", "female")
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_non_equal_email_signup", result, "Invalid Signup")

    @pytest.mark.run(order=10)
    def test_valid_signup(self):
        # we should put new email that is not exist in the database
        self.su.signup("modyseka@gmail.com", "modyseka@gmail.com", "2222222222", "sayed", "27", 2, "1999", "male")
        # we should change it after th integration with the other teams
        result = self.su.verifyLoginFailed()
        self.ts.markFinal("test_valid_signup", result, "sign up done successsfly")
        # self.su.logout_fn()

    # all the coming tests are having problem + that they have user name and display name that is saved in the database

    @pytest.mark.run(order=11)
    def test_zfacebook(self):
        self.fsu = signuppage_f(self.driver)
        self.fsu.click_signup_facebook()
        parentHandle = self.driver.current_window_handle
        handles = self.driver.window_handles
        self.fsu.switch_handles_login(parentHandle, handles, self.driver, "01150297934", "Mohammed.33")
        self.driver.switch_to.window(parentHandle)
        time.sleep(5)
        self.fsu.logout_fn()
        self.driver.quit()

        # result = self.su.verifyLoginSuccessful()
        # self.ts.markFinal("test_zfacebook", result, "sign up done successsfly")
        # time