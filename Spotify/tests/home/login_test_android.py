import time
from pages.home.Login_page_Android import LoginPage
from appium import webdriver
import unittest


class LoginTestAndroid(unittest.TestCase):

    def test_validlogin(self):
        desired_Cap = {
  "platformName": "Android",
  "deviceName": "Pixel 3a",
  "platformVersion": "8",
  "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
}
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("","2222222222")
        lp.login("modyseka@gamil.com","")
        lp.login("","")
        lp.login("ahmed", "2222222222")
        lp.ClickShowPassword()
        lp.login("ahmed@.com", "2222222222")
        lp.ClickShowPassword()
        lp.login("ahmed@gmail.", "2222222222")
        lp.ClickShowPassword()
        lp.login("ahmed@@gmail.com", "2222222222")
        lp.ClickShowPassword()
        lp.login("@gmail.com", "2222222222")
        lp.ClickShowPassword()
        lp.login("ahmed@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", "2222222222")
        lp.ClickShowPassword()
        lp.login("ahmed@gmail.com", "2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")
        lp.ClickShowPassword()
        lp.final_login("modyseka@gmail.com", "3333333333")
        lp.log_out()
        lp.forgetpassword("fdskf")
        lp.clear_forget_email()
        lp.EnterForgetEmail("ahmed@.com")
        lp.clear_forget_email()
        lp.EnterForgetEmail("ahmed@gmail.")
        lp.clear_forget_email()
        lp.EnterForgetEmail("ahmed@@gmail.com")
        lp.clear_forget_email()
        lp.EnterForgetEmail("@gmail.com")
        lp.clear_forget_email()
        lp.EnterForgetEmail("modyseka@gmail.com")
        lp.ClickGetLink()
#         # lp.login_facebook("tspotif36y@yahoo.com","ahmedgaber")
        # lp.forgetpassword("abc")

    def test_invalidlogin1(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("", "2222222222")

    def test_invalidlogin2(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("modyseka@gamil.com","" )

    def test_invalidlogin3(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("","")


    def test_invalidlogin4(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed", "2222222222")

    def test_invalidlogin5(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed@.com", "2222222222")

    def test_invalidlogin6(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed@gmail.", "2222222222")

    def test_invalidlogin7(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed@@gmail.com", "2222222222")


    def test_invalidlogin8(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("@gmail.com", "2222222222")


    def test_invalidlogin9(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", "2222222222")


    def test_invalidlogin10(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("ahmed@gmail.com", "2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222")


    def test_validlogin11(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("modyseka@gmail.com", "3333333333")
        lp.ClickLoginButton()


    def test_forget_password_1(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("fdskf")
        time.sleep(5)

    def test_forget_password_2(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("ahmed@.com")
        time.sleep(5)

    def test_forget_password_3(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("ahmed@gmail.")
        time.sleep(5)

    def test_forget_password_4(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("ahmed@@gmail.com")
        time.sleep(5)

    def test_forget_password_5(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("@gmail.com")
        time.sleep(5)

    def test_forget_password_6(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.forgetpassword("modyseka@gmail.com")
        time.sleep(5)

    def test_login_logout(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (3).apk"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        lp = LoginPage(driver)
        time.sleep(1)
        lp.Homelogin("modyseka@gmail.com", "3333333333")
        lp.ClickLoginButton()
        time.sleep(3)
        lp.log_out()
