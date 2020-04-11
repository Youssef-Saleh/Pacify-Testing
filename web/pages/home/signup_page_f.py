from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import time
import logging
import web.utilities.custom_logger as cl

class signuppage_f(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver=Driver

    #locators
    SignupLink= "Sign up"
    #ContinueFacebook= "select-button-signup-fb"
    Facebook="SIGN UP WITH FACEBOOK"
    ProfileLink= "svelte-kdyqkb"
    EmailField= "email"
    PasswordField= "pass"
    SubmitBtn= "login"
    ProfileClass= "svelte-kdyqkb"
    LogoutBtn = "Log Out"
    def ClickFacebook(self):
        self.ElementClick(self.Facebook,"link")
    def LogoutFN(self):
        self.ClickProfileLink()
        self.ClickLogoutBtn()

    def ClickProfileLink(self):
        self.ElementClick(self.ProfileClass, LocatorType="class")

    def ClickLogoutBtn(self):
        self.ElementClick(self.LogoutBtn, LocatorType="link")
        ################################################
    def ClickSignupFacebook(self):
        self.ElementClick(self.ContinueFacebook, LocatorType="id")
    def EnterEmail(self, email):
        self.SendKeys(email, self.EmailField)
    def EnterPassword(self, password):
        self.SendKeys(password, self.PasswordField)
    def login(self):
        self.ElementClick(self.SubmitBtn, LocatorType="name")
    def SignupFacebook(self, email="", password=""):
        self.EnterEmail(email)
        self.EnterPassword(password)
        self.login()


    def SwitchhandlesLogin(self, parenthandle, handles, driver, email, password):
        result=self.IsElementPresent(self.ProfileLink, LocatorType="CLASS_NAME")
        if result == True:
            time.sleep(2)
            return
        else:
            for handle in handles:
                if handle not in parenthandle:
                    driver.switch_to.window(handle)
                    handles = driver.window_handles
                    break
            self.SignupFacebook(email, password)