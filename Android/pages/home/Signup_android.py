from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
from appium.webdriver.common.touch_action import TouchAction
import logging
import web.utilities.custom_logger as cl
import time
class signuppage_android(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver=Driver

    #locators
    _signup_link_free="signUp_button"
    _email_android="signUp_Email_editText"
    NextBtnEmail= "signUp_email_Next_button"
    _password_android="signUp_Password_editText"
    _confirm_password="signUp_Password_confirm_editText"
    NextBtnPassword= "signUp_password_Next_button"
    Month="	/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText"
    Day="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText"
    Year="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.DatePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[3]/android.widget.EditText"
    NextBtnDate="signUp_dob_Next_button"
    PhoneNumber="signup_phone_number_text"
    NextBtnPhone="signup_phone_number_confirm_button"
    Male="male_button"
    Female="female_button"
    BackGender="signUp_gender_Back_button"
    DisplayName="signUp_Name_editText"
    Create="signUp_Name_Create_button"
    BackDisplay="signUp_Name_Back_button"
    def click_signup_link_A(self):
        self.ElementClick(self._signup_link_free, LocatorType="id")
    def SendkeysEmail(self, email):
        self.SendKeys(email, self._email_android, LocatorType="id")
    def ClickNextBtnEmail(self):
        self.ElementClick(self.NextBtnEmail, LocatorType="id")
    def SendkeysPassword(self, password):
        self.SendKeys(password, self._password_android, LocatorType="id")
    def SendkeysCPassword(self, cpassword):
        self.SendKeys(cpassword, self._confirm_password, LocatorType="id")
    def ClickNextPassword(self):
        self.ElementClick(self.NextBtnPassword, LocatorType="id")
    def clickNextBtnDate(self):
        self.ElementClick(self.NextBtnDate,LocatorType="id")
    def ActionDay(self,Day):
        Actions = TouchAction(self.Driver)
        Actions.long_press(self.Day,duration=100)
        Actions.scroll(10, 100)
        Actions.perform()
        #self.SendKeys(Day,self.Day,LocatorType="xpath")
    def ActionMonth(self,Month):
        a=""
    def ActionYear(self,Year):
        a=""
    def ClickNextDate(self):
        self.ElementClick(self.NextBtnDate,LocatorType="id")
    def SendPhoneNumber(self,Phone):
        self.SendKeys(Phone,self.PhoneNumber,LocatorType="id")
    def ClickNextBtnPhone(self):
        self.ElementClick(self.NextBtnPhone,LocatorType="id")
    def ChooseGender(self,Gender):
        if Gender == "Male" or "male":
            self.ElementClick(self.Male,LocatorType="id")
        else:
            self.ElementClick(self.Female,LocatorType="id")
    def ClickBackGender(self):
        self.ElementClick(self.BackGender,LocatorType="id")
    def ClickBackDisplay(self):
        self.ElementClick(self.BackDisplay,LocatorType="id")
    def CreateNewEmail(self):
        self.ElementClick(self.Create,LocatorType="id")
    def SendKeysDisplayName(self,DisplayName):
        self.SendKeys(DisplayName,self.DisplayName,LocatorType="id")
    def SignupAndroid(self,Email,Password,ConfirmPassword,PhoneNumber,Gender,DisplayName):
        self.click_signup_link_A()
        time.sleep(0.25)
        self.SendkeysEmail(Email)
        self.ClickNextBtnEmail()
        time.sleep(0.25)
        self.SendkeysPassword(Password)
        self.SendkeysCPassword(ConfirmPassword)
        self.ClickNextPassword()
        time.sleep(0.25)
        self.ClickNextDate()
        #back
        self.SendPhoneNumber(PhoneNumber)
        self.ClickNextBtnPhone()
        time.sleep(0.25)
        self.ChooseGender(Gender)
        time.sleep(0.25)
        self.SendKeysDisplayName(DisplayName)
        self.CreateNewEmail()
        time.sleep(0.25)






