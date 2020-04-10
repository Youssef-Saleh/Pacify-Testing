from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import time
import logging
import web.utilities.custom_logger as cl

class signuppage_f(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    #locators
    _signup_link="Sign up"
    _continue_fcebook="select-button-signup-fb"
    _profile_tab="svelte-kdyqkb"
    _email_field="email"
    _password_field="pass"
    _submit_button="login"
    _profile_class="svelte-kdyqkb"
    _logout_btn = "Log Out"

    def logout_fn(self):
        self.click_profile_tab()
        self.click_logout_btn()

    def click_profile_tab(self):
        self.elementClick(self._profile_class, locatorType="class")

    def click_logout_btn(self):
        self.elementClick(self._logout_btn, locatorType="link")
        ################################################
    def click_signup_facebook(self):
        self.elementClick(self._continue_fcebook,locatorType="id")
    def enter_email(self, email):
        self.sendKeys(email, self._email_field)
    def enter_password(self,password):
        self.sendKeys(password,self._password_field)
    def login(self):
        self.elementClick(self._submit_button,locatorType="name")

    def signup_facebook(self,email="",password=""):
        self.enter_email(email)
        self.enter_password(password)
        self.login()


    def switch_handles_login(self,parenthandle,handles,driver,email,password):
        result=self.isElementPresent(self._profile_tab,locatorType="CLASS_NAME")
        if result == True:
            time.sleep(2)
            return
        else:
            for handle in handles:
                if handle not in parenthandle:
                    driver.switch_to.window(handle)
                    handles = driver.window_handles
                    break
            self.signup_facebook(email,password)