
import traceback
from appium import webdriver

class WebDriverFactory():

    #def __init__(self, browser):

        #self.browser = browser


    def configuration(self):
        self.driver = webdriver.Remote(
            command_executor="http://localhost:4723/wd/hub",
            desired_capabilities={
                "platformName": "Android",
                "platformVersion": "7.1.1",
                "deviceName": "sayed",
                "app": "C:\\Users\\Eslam\\Downloads\\app-debug .apk",
                "automationName": "uiautomator2",
                "noSign": "true"
            }
        )
        return self.driver