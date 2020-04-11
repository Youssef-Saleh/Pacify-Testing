from appium import webdriver
from Android.pages.home.Signup_android import signuppage_android
from Android.base.appium_driver import AppiumDriver
from Android.pages.home.home_page import homepage
from Android.pages.home.Library import Library
import time


#@pytest.mark.usefixtures("A_oneTime_signup_SetUp", "A_signup_setUp")
#class Testsignup_A(unittest.TestCase, SeleniumDriver):
#    @pytest.fixture(autouse=True)
#    def signupSetup(self, A_oneTime_signup_SetUp):
#        self.su = signuppage_android(self.Driver)
#        self.ts = TestStatus(self.Driver)

#    @pytest.mark.run(order=1)
#    def test_A_invalid_signup(self):
#        self.Driver.click_signup_link_A()

class signup_android_test(AppiumDriver):
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
    su=signuppage_android(Driver)
    su.SignupAndroid("done@gmail.com","Mohammed.33S","Mohammed.33S","01150297934","male","sayed")
    hp=homepage(Driver)
    hp.click_login()
    Driver.back()
    li.Login("sayed@gmail.com", "2222222222")
    time.sleep(0.25)
    li.ClickLibrary()
    li.ClickSetting()
    time.sleep(0.25)
    li.ClickLogout()
    time.sleep(3)
    hp.click_facebook()
    Driver.back()
    Driver.quit()

