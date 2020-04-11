import time
from pages.home.Edit_android import Edit_Android
from appium import webdriver
import unittest

class EditTest(unittest.TestCase):


    def test_edit(self):
        desired_Cap = {
  "platformName": "Android",
  "deviceName": "Pixel 3a",
  "platformVersion": "8",
  "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
}
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        edit = Edit_Android(driver)
        edit.login_edit("A@g.c", "1111")
        edit.edit_email_with_change_mind()
        edit.click_edit()
        edit.click_change_email_button()
        edit.edit_email_without_button("ahmed")
        edit.edit_email_without_button("ahmed@.com")
        edit.edit_email_without_button("ahmed@gmail.")
        edit.edit_email_without_button("ahmed@@gmail.com")
        edit.edit_email_without_button("@gmail.com")
        edit.edit_email_without_button("ahmed@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        edit.edit_email_with_button("modyseka@gmail.com")
        edit.edit_password_with_change_mind_full()
        edit.click_edit()
        edit.click_change_password_button()
        edit.edit_password_without_button("a", "ahmedgaber10", "ahmedgaber10")
        edit.edit_password_with_button("a", "Ahmedgaber10", "ahmedgaber10")
        edit.click_edit()
        edit.click_change_password_button()
        edit.edit_password_with_button("a", "Ahmedgaber10", "Ahmedgaber1")
        edit.click_edit()
        edit.click_change_password_button()
        edit.edit_password_without_button("", "Ahmedgaber10", "Ahmedgaber10")
        edit.edit_password_without_button("a", "Ahmedgaber", "Ahmedgaber")
        edit.edit_password_without_button("a", "Ag10", "Ag10")
        edit.edit_password_without_button("a", "AHMEDGABER10", "AHMED10GABER")
        edit.edit_password_without_button("a", "Ahmed gaber10", "Ahmed gaber10")
     #   edit.edit_password_with_button("a", "Ag10zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz","Ag10zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        edit.edit_password_without_button("a", "!@#$%^&*()", "!@#$%^&*()")
     #   edit.edit_password_with_button("Ahmedgaber10", "Ahmedgaber10", "Ahmedgaber10")
        edit.edit_password_with_button("a","Ahmedgaber10","Ahmedgaber10")
        edit.edit_country_with_change_mind_full()
        edit.click_edit()
        edit.click_change_country_button()
        edit.edit_country_without_done("hamada")
        edit.edit_country_without_done("ad@dfkd")
        edit.edit_country_without_done("hfhf465456489diwhffabg")
        edit.edit_country_without_done("46454684884694")
        edit.edit_country_with_done("egypt")
        edit.edit_phone_with_change_mind_full()
        edit.click_edit()
        driver.implicitly_wait(2)
        edit.click_change_phone_button()
        edit.edit_phone_without_done("hamada")
        edit.edit_phone_without_done("ad@dfkd")
        edit.edit_phone_without_done("hfhf465456489diwhffabg")
        edit.edit_phone_without_done("46454684884694")
        edit.edit_phone_without_done("4989989")
        edit.edit_phone_with_done("01033811138")
        edit.edit_gender_with_change_mind_full()
        edit.edit_gender_Male()
        edit.edit_gender_Female()
     #    edit.edit_date_with_change_mind()
     #    edit.click_edit()
     #    edit.click_change_date_button()
     #    edit.edit_date("2", "apr", "2018")

    def test_edit_email(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        edit = Edit_Android(driver)
        edit.login_edit("A@g.c", "1111")
        edit.edit_email_with_change_mind()
        edit.click_edit()
        edit.click_change_email_button()
        edit.edit_email_without_button("ahmed")
        edit.edit_email_without_button("ahmed@.com")
        edit.edit_email_without_button("ahmed@gmail.")
        edit.edit_email_without_button("ahmed@@gmail.com")
        edit.edit_email_without_button("@gmail.com")
        edit.edit_email_without_button("ahmed@gmail.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        edit.edit_email_with_button("modyseka@gmail.com")

    def test_edit_password(self):
           desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
        }
           driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
           edit = Edit_Android(driver)
           edit.login_edit("A@g.c", "1111")
           edit.edit_password_with_change_mind()
           edit.click_edit()
           edit.click_change_password_button()
           edit.edit_password_without_button("a", "ahmedgaber10", "ahmedgaber10")
           edit.edit_password_with_button("a", "Ahmedgaber10", "ahmedgaber10")
           edit.click_edit()
           edit.click_change_password_button()
           edit.edit_password_with_button("a", "Ahmedgaber10", "Ahmedgaber1")
           edit.click_edit()
           edit.click_change_password_button()
           edit.edit_password_without_button("", "Ahmedgaber10", "Ahmedgaber10")
           edit.edit_password_without_button("a", "Ahmedgaber", "Ahmedgaber")
           edit.edit_password_without_button("a", "Ag10", "Ag10")
           edit.edit_password_without_button("a", "AHMEDGABER10", "AHMED10GABER")
           edit.edit_password_without_button("a", "Ahmed gaber10", "Ahmed gaber10")
        #   edit.edit_password_with_button("a", "Ag10zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz","Ag10zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
           edit.edit_password_without_button("a", "!@#$%^&*()", "!@#$%^&*()")
           edit.edit_password_with_button("Ahmedgaber10", "Ahmedgaber10", "Ahmedgaber10")
           # edit.edit_password_with_button("a","Ahmedgaber10","Ahmedgaber10")

    def test_edit_country(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        edit = Edit_Android(driver)
        edit.login_edit("A@g.c", "1111")
        edit.edit_country_with_change_mind()
        edit.click_edit()
        edit.click_change_country_button()
        edit.edit_country_without_done("hamada")
        edit.edit_country_without_done("ad@dfkd")
        edit.edit_country_without_done("hfhf465456489diwhffabg")
        edit.edit_country_without_done("46454684884694")
        edit.edit_country_with_done("egypt")

    def test_edit_phone(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        edit = Edit_Android(driver)
        edit.login_edit("A@g.c", "1111")
        edit.edit_phone_with_change_mind()
        edit.click_edit()
        driver.implicitly_wait(2)
        edit.click_change_phone_button()
        edit.edit_phone_without_done("hamada")
        edit.edit_phone_without_done("ad@dfkd")
        edit.edit_phone_without_done("hfhf465456489diwhffabg")
        edit.edit_phone_without_done("46454684884694")
        edit.edit_phone_without_done("4989989")
        edit.edit_phone_with_done("01033811138")

    def test_edit_gender(self):
        desired_Cap = {
            "platformName": "Android",
            "deviceName": "Pixel 3a",
            "platformVersion": "8",
            "app": "C:\\Users\\Mohamed Gaber\\Downloads\\app-debug (2).apk"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_Cap)
        edit = Edit_Android(driver)
        edit.login_edit("A@g.c", "1111")
        edit.edit_gender_with_change_mind()
        edit.edit_gender_Male()
        edit.edit_gender_Female()





