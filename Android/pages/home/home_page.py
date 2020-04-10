from appium import webdriver
from Android.base.appium_driver import AppiumDriver
import logging
import Android.utilities.custom_logger_and as cl

class homepage(AppiumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver
    #locators

    _signup_tab="signUp_button"
    _Login_tab="login_button"
    _facebook="login_forget_password_button"


    ###########################################################
    def click_sign_up(self):
        self.elementClick(self._signup_tab,locatorType="id")
    def click_login(self):
        self.elementClick(self._Login_tab,locatorType="id")
    def click_facebook(self):
        self.elementClick(self._facebook,locatorType="id")