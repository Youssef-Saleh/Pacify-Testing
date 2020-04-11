import time
from selenium import webdriver
from pages.home.Login_page_project import LoginPage
import unittest


class LoginTest(unittest.TestCase):

    def test_login_valid(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("http://23.96.41.241/")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        lp = LoginPage(Driver)
        time.sleep(1)
        lp.HomeLoginS("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        Driver.quit()


    def test_invalid_login_1(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("http://23.96.41.241/")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        lp = LoginPage(Driver)
        lp.HomeLogin("editingmaster@artist.pacify", "")
        time.sleep(5)
        Driver.quit()

    def test_invalid_login_2(self):
        Driver = webdriver.Chrome(
               executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("http://23.96.41.241/")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        lp = LoginPage(Driver)
        lp.HomeLogin("", "")
        time.sleep(5)
        Driver.quit()

    def test_invalid_login_3(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("", "")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_4(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "abc")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_5(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@gmail.com", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_6(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("ahmed.gaber42@yahoo.com", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_7(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_8(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacifyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
                     "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"
                     "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_9(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek222222222222222222222222222222222222222"
                                                    "22222222222222222222222222222222222222222222222222"
                                                    "222222222222222222222222222222222222222222222222")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_10(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_11(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_12(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_13(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        lp.ClickLoginLink()
        time.sleep(5)
        driver.quit()

    def test_invalid_login_shortpassword(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("ahmed.gaber428@yahoo.co", "1234")
        time.sleep(2)
        driver.quit()

    def test_forward_login(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.quit()

    def test_invalid_login_shortpassword_email(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("ahmed", "12345")
        time.sleep(2)
        driver.quit()

    def test_invalid_login_14(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        lp.ClickLoginLink()
        lp.Login("ahmed.gaber428@yahoo.com", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_invalid_login_15(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(2)
        driver.back()
        time.sleep(2)
        lp.ClickLoginLink()
        lp.Login("editingmaster@artist.pacify", "Dehkmodhek")
        time.sleep(5)
        driver.quit()



    def test_spotify_logo_and_failed_login(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.HomeLogin("editingmaster@artist.pacify", "Dehkmodhek")
        time.sleep(1)
        lp.Login("aaaaaa", "aaaaaaaaaa")
        time.sleep(1)
        lp.Login("ajsjash", "jakasdklasd")
        i = 0
        while (i < 100):
            lp.ClickLoginButton()
            i = i + 1
        lp.ClickSpotify()
        time.sleep(1)
        lp.ClickLoginLink()
        lp.Login("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(10)
        driver.quit()

    def test_remeber_me(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.LoginWithRemember("editingmaster@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        driver.quit()

    def test_forget_password(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.ForgetPassword("ahmed.gaber428@yahoo.com")
        time.sleep(3)
        driver.quit()

    def test_forget_password_2(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.ForgetPassword("010333")
        driver.quit()

    def test_login_facebook(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.LoginFacebook("01033811138", "ahmedgaber")
        time.sleep(5)
        driver.quit()

    def test_apple(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.TestApple()
        driver.quit()

    def test_stress1(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.StressLogin1()
        time.sleep(3)
        driver.quit()

    def test_stress2(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.StressLogin2()
        time.sleep(3)
        driver.quit()

    def test_stress3(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.StressLogin3()
        time.sleep(3)
        driver.quit()

    def test_stress4(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.StressLogin4()
        time.sleep(3)
        driver.quit()

    def test_stress5(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        lp = LoginPage(driver)
        lp.StressLogin5()
        time.sleep(3)
        driver.quit()






