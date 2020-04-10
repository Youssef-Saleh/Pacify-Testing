from Android.base.appium_driver import AppiumDriver
from Android.pages.home.home_page import homepage
from appium import webdriver

class home_test(AppiumDriver):
    driver = webdriver.Remote(
        command_executor="http://localhost:4723/wd/hub",
        desired_capabilities={
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "sayed",
            "app": "C:\\Users\\Eslam\\Downloads\\app-debug (1).apk",
            "automationName": "uiautomator2",
            "noSign": "true"
        }

    )
    hp=homepage(driver)
    hp.click_login()
    driver.back()
    hp.click_sign_up()
    driver.back()
    hp.click_facebook()
    driver.back()