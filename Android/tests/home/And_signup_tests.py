from appium import webdriver
from Android.pages.home.Signup_android import signuppage_android
from Android.base.appium_driver import AppiumDriver


#@pytest.mark.usefixtures("A_oneTime_signup_SetUp", "A_signup_setUp")
#class Testsignup_A(unittest.TestCase, SeleniumDriver):
#    @pytest.fixture(autouse=True)
#    def signupSetup(self, A_oneTime_signup_SetUp):
#        self.su = signuppage_android(self.driver)
#        self.ts = TestStatus(self.driver)

#    @pytest.mark.run(order=1)
#    def test_A_invalid_signup(self):
#        self.driver.click_signup_link_A()

class signup_android_test(AppiumDriver):
    webdriver = webdriver.Remote(
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
    su=signuppage_android(webdriver)
    su.click_signup_link_A()
    su.sendkeys_email("modyseka@gmail.com")
    su.click_next_button()
    webdriver.implicitly_wait(3)
    su.sendkeys_password("11111111")
    su.sendkeys_cpassword("11111111")
    su.click_next_button()

