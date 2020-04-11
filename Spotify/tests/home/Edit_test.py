import time
from selenium import webdriver
from pages.home.Account_overview import AccountPage
import unittest

class EditAccount(unittest.TestCase):

    email1 = "modyseka@gmail.com"
    email2 = "ahmed.gaber428@yahoo.com"
    password = "789456123"
    mobile1 = "01150297934"
    mobile2 = "01033811138"


    def test_Account_phone_only(self):
        Driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        Driver.get("https://www.spotify.com/eg-en//")
        Driver.maximize_window()
        Driver.implicitly_wait(5)
        edit = AccountPage(Driver)
        edit.log_in_edit(self.email1, "3333333333")
        edit.edit_mobile_no("abc")
        edit.edit_mobile_no("abc@gmailcom")
        edit.edit_mobile_no("0")
        edit.edit_mobile_no("0258956599999999999999999999999999999999999999999999999999999999999999")
        edit.edit_mobile_no(self.mobile2)
        Driver.quit()

    def test_Account_years_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")
        edit.edit_year_full("0000")
        time.sleep(0.5)
        edit.edit_year_full("2000")
        time.sleep(0.5)
        edit.edit_year_full("1900")
        time.sleep(2)
        driver.quit()

    def test_Account_days_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")
        edit.edit_day_full("32")
        edit.edit_day_full("20")
        time.sleep(2)
        driver.quit()

    def test_Account_monthes_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")
        edit.edit_month_full("00")
        edit.edit_month_full("13")
        edit.edit_month_full("03")
        time.sleep(2)
        driver.quit()

    def test_Account_gender_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")
        edit.edit_gender_full("Female")
        edit.edit_gender_full("asm")
        edit.edit_gender_full("Male")
        time.sleep(2)
        driver.quit()

    def test_Account_date_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")

        edit.change_brith_date("31", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "04", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "06", "1998")
        time.sleep(0.5)
        edit.change_brith_date("31", "09", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "11", "1998")
        time.sleep(1)
        edit.change_brith_date("30", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("29", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("30", "04", "1999")
        time.sleep(0.5)
        edit.change_brith_date("29", "02", "1996")
        time.sleep(1)
        edit.change_brith_date("31", "03", "1998")
        time.sleep(2)
        driver.quit()

    def test_Account_email_only(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "3333333333")
        edit.edit_email_full(self.password, self.email2)
        time.sleep(0.5)
        edit.logout_edit()
        edit.log_in_edit(self.email2, "3333333333")
        edit.edit_email_full("3333333333", "a@yahoo.com")
        time.sleep(1)
        edit.edit_email_full("123", self.email1)
        time.sleep(1)
        edit.edit_email_full(self.password, self.email1)
        time.sleep(1)
        edit.edit_email_full(self.password, "abcd")
        time.sleep(1)
        edit.edit_email_full(self.password, "1234")
        time.sleep(1)
        edit.edit_email_full(self.password, "modyseka@.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "modyseka@gmail")
        time.sleep(1)
        edit.edit_email_full(self.password, "modyseka@@gmail.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "@gmail.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "modyseka@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        time.sleep(1)
        edit.edit_email_full(self.password, "")
        time.sleep(5)
        driver.quit()

    def test_Account_change_all(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "2222222222")
        edit.change_all(self.email2, self.password, "Female", "15", "05", "1995", self.mobile2)
        time.sleep(1)
        edit.change_all("a@yahoo.com", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1.5)
        edit.change_all("abc", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        edit.change_all("123", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        edit.change_all("", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        # edit.change_all(self.email1, "123", "Male", "10", "09", "1997", self.mobile1)
        # time.sleep(1)
        edit.change_all(self.email1, self.password, "Male", "10", "09", "1998", self.mobile1)
        time.sleep(1)
        edit.change_all(self.email2, self.password, "Male", "31", "11", "1997", self.mobile1)
        time.sleep(1)
        driver.quit()

    def test_Account_change_password(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, self.password)
        driver.implicitly_wait(5)
        edit.change_password("", "", "")
        edit.change_password(self.password, "", "25252525")
        edit.change_password(self.password, "25252525", "")
        edit.change_password("", "25252525", "25252525")
        edit.change_password(self.password, self.password, self.password)
        edit.change_password(self.password, "a", "a")
        edit.change_password(self.password, "ag195", "ag195")
        edit.change_password(self.password, "25252525", "252525")
        edit.change_password(self.password, "25252", "25252525")
        edit.change_password("11111", "25252525", "25252525")
        edit.change_password(self.password, "!@#$%^&*()", "!@#$%^&*()")
        edit.change_password(self.password, "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
                              , "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")

    def test_Account_phone_only_facebook(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.login_facebook_edit("01033811138","ahmedgaber")
        edit.edit_mobile_no_facebook("abc")
        time.sleep(1)
        edit.edit_mobile_no_facebook("0")
        time.sleep(1)
        edit.edit_mobile_no_facebook("02589")
        time.sleep(1)
        edit.edit_mobile_no_facebook(self.mobile2)
        time.sleep(2)
        driver.quit()


    def test_Account_change_password_email(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, "3333333333")
        driver.implicitly_wait(5)
        edit.change_password_email("3333333333", "", "", self.email1)

        driver.quit()


    def full_test_edit(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        edit = AccountPage(driver)
        edit.log_in_edit(self.email1, self.password)
        ########################################################
        ###################change mobile#####################
        edit.edit_mobile_no("abc")
        edit.edit_mobile_no("abc@gmailcom")
        edit.edit_mobile_no("0")
        edit.edit_mobile_no("0258956599999999999999999999999999999999999999999999999999999999999999")
        edit.edit_mobile_no(self.mobile2)
        driver.refresh()
        driver.implicitly_wait(3)
        ########################################################
        ###################change year#####################
        edit.edit_year_full("0000")
        time.sleep(0.5)
        edit.edit_year_full("2000")
        time.sleep(0.5)
        edit.edit_year_full("1900")
        driver.refresh()
        driver.implicitly_wait(5)
        ########################################################
        ###################change day#####################
        edit.edit_day_full("00")
        edit.edit_day_full("32")
        time.sleep(1)
        edit.edit_day_full("20")
        driver.refresh()
        driver.implicitly_wait(5)
        ########################################################
        ###################change month#####################
        edit.edit_month_full("00")
        time.sleep(1)
        edit.edit_month_full("07")
        driver.refresh()
        driver.implicitly_wait(3)
        ##########################################################
        ###################change gender##################
        edit.edit_gender_full("Female")
        edit.edit_gender_full("asm")
        time.sleep(2)
        edit.edit_gender_full("Male")
        driver.refresh()
        driver.implicitly_wait(5)
        #######################################################
        #############change date#######################
        edit.change_brith_date("31", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "04", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "06", "1998")
        time.sleep(0.5)
        edit.change_brith_date("31", "09", "1998")
        time.sleep(1)
        edit.change_brith_date("31", "11", "1998")
        time.sleep(1)
        edit.change_brith_date("30", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("29", "02", "1998")
        time.sleep(1)
        edit.change_brith_date("30", "04", "1999")
        time.sleep(0.5)
        edit.change_brith_date("29", "02", "1996")
        time.sleep(1)
        edit.change_brith_date("31", "03", "1998")
        time.sleep(2)
        driver.refresh()
        driver.implicitly_wait(5)
        ##################################################################
        #############change email###################################
        edit.click_edit_profile_menu()
        driver.implicitly_wait(5)
        edit.edit_email_full(self.password, self.email2)
        time.sleep(0.5)
        edit.logout_edit()
        edit.log_in_edit(self.email2, "3333333333")
        edit.edit_email_full("3333333333", "a@yahoo.com")
        time.sleep(1)
        edit.edit_email_full("123", self.email1)
        time.sleep(1)
        edit.edit_email_full(self.password, self.email1)
        time.sleep(1)
        edit.edit_email_full(self.password, "abcd")
        time.sleep(1)
        edit.edit_email_full(self.password, "1234")
        time.sleep(1)
        edit.edit_email_full(self.password, "ahmed@.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "ahmed@gmail")
        time.sleep(1)
        edit.edit_email_full(self.password, "ahmed@@gmail.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "@gmail.com")
        time.sleep(1)
        edit.edit_email_full(self.password, "ahmed@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        time.sleep(1)
        edit.edit_email_full(self.password, "")
        time.sleep(5)
        #################################################
        ###change all#######################
        driver.refresh()
        driver.implicitly_wait(5)
        edit.change_all(self.email2, self.password, "Female", "15", "05", "1995", self.mobile2)
        time.sleep(1)
        edit.change_all("a@yahoo.com", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1.5)
        edit.change_all("abc", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        edit.change_all("123", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        edit.change_all("", self.password, "Male", "10", "09", "1997", self.mobile1)
        time.sleep(1)
        # edit.change_all(self.email1, "123", "Male", "10", "09", "1997", self.mobile1)
        # time.sleep(1)
        edit.change_all(self.email1, self.password, "Male", "10", "09", "1998", self.mobile1)
        time.sleep(1)
        edit.change_all(self.email2, self.password, "Male", "31", "11", "1997", self.mobile1)
        time.sleep(1)
        ##########################################################
        #####################change password######################
        edit.change_password("", "", "")
        time.sleep(1)
        edit.change_password(self.password, "", "25252525")
        time.sleep(1)
        edit.change_password(self.password, "25252525", "")
        time.sleep(1)
        edit.change_password("", "25252525", "25252525")
        time.sleep(1)
        edit.change_password(self.password, self.password, self.password)
        time.sleep(1)
        edit.change_password(self.password, "a", "a")
        time.sleep(1)
        edit.change_password(self.password, "ag195", "ag195")
        time.sleep(1)
        edit.change_password(self.password, "25252525", "252525")
        time.sleep(1)
        edit.change_password(self.password, "25252", "25252525")
        time.sleep(1)
        edit.change_password("11111", "25252525", "25252525")
        time.sleep(1)
        edit.change_password(self.password, "!@#$%^&*()", "!@#$%^&*()")
        time.sleep(1)
        # edit.change_password(self.password, "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
        #                      , "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        time.sleep(1)
        ##########################################################
        #####################change email password######################
        # edit.change_password_email("4444444444", "4444444444", "4444444444", self.email2)
        ######################################################################
        #########################facebook##################################
        edit.logout_edit()
        driver.implicitly_wait(5)
        edit.login_facebook_edit("01033811138","ahmedgaber")
        edit.edit_mobile_no_facebook("abc")
        time.sleep(1)
        edit.edit_mobile_no_facebook("0")
        time.sleep(1)
        edit.edit_mobile_no_facebook("02589")
        time.sleep(1)
        edit.edit_mobile_no_facebook(self.mobile2)
        time.sleep(2)
        edit.edit_mobile_no_facebook("55555555555555555555555555555555555555555555555")
        time.sleep(2)



test = EditAccount()

test.full_test_edit()