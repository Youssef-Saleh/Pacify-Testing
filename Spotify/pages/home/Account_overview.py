from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time

class AccountPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver


#Locators
    Loginlink = "Log In"   #link
    Editprofile = "Edit profile"    #link
    emailfield = "login-username" #id
    gender = "profile_gender"#id
    monthes = "profile_birthdate_month"#id
    days = "profile_birthdate_day"#id
    years = "profile_birthdate_year"#id
    mobile = "profile_mobile_number"#id
    save_profile = "profile_save_profile"#id
    cancel = "profile_cancel"#id
    passwordfield = "login-password"
    loginbutton = "login-button"
    confirm_password = "profile_confirmPassword" #id
    profile_email = "profile_email" #id
    menu = "svelte-kdyqkb"
    logout = "Log Out"
    Remember_me ="control-indicator"
    changepassword = "/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div/ul/li[3]/a" #Xpath
    edit_profile = "/html/body/div[2]/div[2]/div[2]/div/div/div[1]/div/ul/li[2]/a" #xpath
    current_password = "change_password_validatePassword" #id
    new_password = "change_password_new_password" #id
    repeat_new_password = "change_password_check_password" #id
    set_new_password = "change_password_submit" #id
    cancel_password = "Cancel"  #link
    facebookbutton = "btn-facebook"
    facebookusername = "email"
    facebookpassword = "pass"
    facebooklogin = "loginbutton"

    def change_email(self, email):
         self.SendKeys(email, self.profile_email)

    def change_gender(self, data):
        self.SelectItem(data, self.gender)

    def change_monthes(self, data):
        self.SelectItem(data, self.monthes)

    def chanege_days(self, data):
        self.SelectItem(data, self.days)

    def change_years(self, data):
        self.SelectItem(data, self.years)

    def change_mobile(self,data):
        self.SendKeys(data, self.mobile)

    def entereamil(self, email):
        self.SendKeys(email, self.emailfield)

    def enterpassword(self, password):
        self.SendKeys(password, self.passwordfield)

    def enter_confirm_password(self, password):
        self.SendKeys(password, self.confirm_password)

    def enter_current_password(self, password):
        self.SendKeys(password, self.current_password)

    def enter_new_password(self, newpassword):
        self.SendKeys(newpassword, self.new_password)

    def enter_repeat_password(self, newpassword):
        self.SendKeys(newpassword, self.repeat_new_password)

    def enterfacebookusername(self, email):
        self.SendKeys(email, self.facebookusername)

    def enterfacebookpassword(self, password):
        self.SendKeys(password, self.facebookpassword)

    def clear_email(self):
        self.Clears(self.emailfield)

    def clear_password(self):
        self.Clears(self.confirm_password)

    def clear_mobile(self):
        self.Clears(self.mobile)

    def clear_current_password(self):
        self.Clears(self.current_password)

    def clear_new_password(self):
        self.Clears(self.new_password)


    def clear_repeat_password(self):
        self.Clears(self.repeat_new_password)

    def clickloginlink(self):
         self.ElementClick(self.Loginlink, "link")

    def clickeditprofile(self):
         self.ElementClick(self.Editprofile, "link")

    def clickmenu(self):
        self.ElementClick(self.menu, "class")

    def clicklogout(self):
        self.ElementClick(self.logout, "link")

    def clickSave(self):
        self.ElementClick(self.save_profile)

    def click_Cancel(self):
        self.ElementClick(self.cancel)

    def clickloginbutton(self):
         self.ElementClick(self.loginbutton)

    def click_change_password(self):
         self.ElementClick(self.changepassword, "xpath")

    def click_edit_profile_menu(self):
         self.ElementClick(self.edit_profile, "xpath")

    def click_save_password(self):
         self.ElementClick(self.set_new_password)

    def click_cancel_password(self):
        self.ElementClick(self.cancel_password, "link")

    def clickremember(self):
        self.ElementClick(self.Remember_me, "class")

    def clickfacebooklogin(self):
        self.ElementClick(self.facebookbutton, "class")

    def clickfacebooktologin(self):
        self.ElementClick(self.facebooklogin)

    def clear_change_email(self):
          self.Clears(self.profile_email)

    def log_in_edit(self, email, password, mobile="0"):
        self.clickloginlink()
        self.entereamil(email)
        self.enterpassword(password)
        self.clickremember()
        self.clickloginbutton()
        self.WaitForElement(self.Editprofile, "link")
        self.clickeditprofile()
        time.sleep(1)
        self.clear_mobile()
        self.SendKeys(mobile, self.mobile)
        self.click_Cancel()
        self.clickeditprofile()


    def logout_edit(self):
        self.clickmenu()
        self.clicklogout()


    def login_facebook_edit(self, username, password):
        self.clickloginlink()
        time.sleep(1)
        self.clickfacebooklogin()
        self.enterfacebookusername(username)
        self.enterfacebookpassword(password)
        self.clickfacebooktologin()
        time.sleep(4)
        self.clickeditprofile()

    def edit_mobile_no_facebook(self, newmobile):
        time.sleep(1)
        self.clear_mobile()
        self.SendKeys(newmobile, self.mobile)
        self.clickSave()


    def edit_mobile_no(self, newmobile):
        self.WaitForElement(self.mobile)
        self.clear_mobile()
        self.SendKeys(newmobile, self.mobile)
        self.clickSave()

    def edit_day_full(self, day):
        self.WaitForElement(self.days)
        self.SelectItem(day, self.days)
        self.clickSave()

    def edit_year_full(self, year):
        self.WaitForElement(self.years)
        self.SelectItem(year, self.years)
        self.clickSave()

    def edit_month_full(self, month):
        self.WaitForElement(self.monthes)
        self.SelectItem(month, self.monthes)
        self.clickSave()

    def edit_email_full(self, password, newemail):
        self.WaitForElement(self.profile_email)
        self.clear_change_email()
        self.clear_password()
        self.change_email(newemail)
        self.enter_confirm_password(password)
        self.clickSave()

    def edit_gender_full(self, gender):
        self.WaitForElement(self.gender)
        self.change_gender(gender)
        self.clickSave()

    def change_brith_date(self, day, month, year):
        self.WaitForElement(self.days)
        self.WaitForElement(self.monthes)
        self.WaitForElement(self.years)
        self.SelectItem(day, self.days)
        self.SelectItem(month, self.monthes)
        self.SelectItem(year, self.years)
        self.clickSave()

    def change_gender_phone(self, newmobile, gender):
        self.SelectItem(gender, self.gender)
        self.clear_mobile()
        self.SendKeys(newmobile, self.mobile)
        self.clickSave()

    def change_all(self, new_email, password, gender, day, month, year, new_mobile):
        self.WaitForElement(self.profile_email)
        self.clear_change_email()
        self.clear_password()
        self.change_email(new_email)
        self.enter_confirm_password(password)
        self.change_gender(gender)
        self.SelectItem(day, self.days)
        self.SelectItem(month, self.monthes)
        self.SelectItem(year, self.years)
        self.clear_mobile()
        self.SendKeys(new_mobile, self.mobile)
        self.clickSave()

    def change_password(self, password, new_password, repeat):
        self.click_change_password()
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(password)
        self.enter_new_password(new_password)
        self.enter_repeat_password(repeat)
        self.click_save_password()

    def change_password_email(self, password, new_password, repeat, newemail):
        self.click_change_password()
        self.clear_current_password()
        self.clear_new_password()
        self.clear_repeat_password()
        self.enter_current_password(password)
        self.enter_new_password(new_password)
        self.enter_repeat_password(repeat)
        self.click_save_password()
        self.click_edit_profile_menu()
        self.clear_change_email()
        self.clear_password()
        self.change_email(newemail)
        self.enter_confirm_password(password)
        self.clickSave()
        self.click_edit_profile_menu()
        self.clear_change_email()
        self.clear_password()
        self.change_email(newemail)
        self.enter_confirm_password(new_password)
        self.clickSave()

