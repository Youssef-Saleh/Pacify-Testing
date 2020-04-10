from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl

class signuppage_android(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver

    #locators
    _signup_link_free="signUp_button"
    _email_android="signUp_Email_editText"
    _next_button="signUp_email_Next_button"
    _password_android="signUp_Password_editText"
    _confirm_password="signUp_Password_confirm_editText"
    _next_button_password=""

    def click_signup_link_A(self):
        self.elementClick(self._signup_link_free,locatorType="id")

    def sendkeys_email(self,email):
        self.sendKeys(email,self._email_android,locatorType="id")

    def click_next_button(self):
        self.elementClick(self._next_button,locatorType="id")

    def sendkeys_password(self,password):
        self.sendKeys(password,self._password_android,locatorType="id")

    def sendkeys_cpassword(self, cpassword):
        self.sendKeys(cpassword, self._confirm_password, locatorType="id")

    def click_next_password(self):
        self.elementClick(self._next_button_password,locatorType="id")



