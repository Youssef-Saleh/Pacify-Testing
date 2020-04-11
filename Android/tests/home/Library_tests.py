from appium import webdriver
from Android.pages.home.Signup_android import signuppage_android
from Android.base.appium_driver import AppiumDriver
import unittest
from Android.pages.home.Library import Library
import time


class Library_test(unittest.TestCase,AppiumDriver):
    Driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "sayed",
            "app": "C:\\Users\\Eslam\\Downloads\\final.apk",
            "automationName": "uiautomator2",
            "noSign": "true"
        }

    )
    li=Library(Driver)
    def test_a(self):
        self.li.Login("sayed@gmail.com","2222222222")
        time.sleep(0.25)
        self.li.ClickLibrary()
        self.li.ClickSetting()
        time.sleep(0.25)
        self.li.ClickLogout()
        self.Driver.quit()

