from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
from selenium.webdriver import ActionChains
import logging
import web.utilities.custom_logger as cl

class signuppage(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver=Driver
    #locators
    SignupLink= "Sign-up"
    EmailField= "/html/body/div/div/div[2]/div[4]/form/div[1]/input"
    ConfirmEmailField= "/html/body/div/div/div[2]/div[4]/form/div[3]/input"
    PasswordField= "/html/body/div/div/div[2]/div[4]/form/div[5]/input"
    DisplayField= "/html/body/div/div/div[2]/div[4]/form/div[7]/input"
    Date="/html/body/div/div/div[2]/div[4]/form/div[9]/input"
    DayField= "register-dob-day"
    MonthField= "register-dob-month"
    YearField= "register-dob-year"
    MaleField= "/html/body/div/div/div[2]/div[4]/form/div[10]/p/label[1]"

    FemaleField= "/html/body/div/div/div[2]/div[4]/form/div[10]/p/label[2]"
    SignupBtn= "/html/body/div/div/div[2]/div[4]/form/div[12]/div[2]/button"
    SpotifyLogo= "/html/body/div[2]/div[2]/div[1]/div/div/a"
    ItemDateClick=""
    LoginLink="Login"
    EmailLoginFieldName="email"
    PasswordLoginFieldName="password"
    LoginBtnLink="/html/body/div/div/div[2]/div[5]/form/div[5]/button"

    ######################################################################
    def ClickLoginLink(self):
        self.ElementClick(self.LoginLink,"link")
    def SendEmailLogin(self,email):
        self.SendKeys(email,self.EmailLoginFieldName,"name")
    def SendPassLogin(self,Pass):
        self.SendKeys(Pass,self.PasswordLoginFieldName,"name")
    def ClickLoginBtn(self):
        self.ElementClick(self.LoginBtnLink,"xpath")
    def LoginFN(self,email,Pass):
        self.ClickLoginLink()
        self.SendEmailLogin(email)
        self.SendPassLogin(Pass)
        self.ClickLoginBtn()

    def ClickSpotifyLogo(self):
        self.ElementClick(self.SpotifyLogo, "xpath")
    def ClickSignupLink(self):
        self.ElementClick(self.SignupLink, LocatorType="link")
    def EnterEmail(self, email):
        self.SendKeys(email, self.EmailField,"xpath")
    def EnterConfirmEmail(self, confirm_email):
        self.SendKeys(confirm_email, self.ConfirmEmailField,"xpath")
    def EnterPassword(self, password):
        self.SendKeys(password, self.PasswordField,"xpath")
    def EnterDisplay(self, display):
        self.SendKeys(display, self.DisplayField,"xpath")
    def EnterDay(self, day):
        self.SendKeys(day, self.DayField)
    def EnterYear(self, year):
        self.SendKeys(year, self.YearField)
    def ClickSignupBtn(self):
        self.ElementClick(self.SignupBtn, LocatorType="xpath")

    def hoverDate(self):
        result = self.Driver.find_element_by_xpath(self.Date)
        Actions=ActionChains(self.Driver)
        Actions.move_to_element(self.FindDate()).perform()

    def SendDate(self,date):
        self.SendKeys(date,self.Date,"xpath")

###########################################################
    def GetMonthField(self):
        return self.Driver.find_element_by_id(self.MonthField)
    def EnterMonth(self, month):
        se=Select(self.GetMonthField())
        se.select_by_index(month)
###########################################################
    def GetAndClickGenderField(self, gender):
        if gender == "male" or "Male":
            type = self.Driver.find_element_by_xpath(self.MaleField)
            type.click()
        elif gender == "Female" or "female":
            type = self.Driver.find_element_by_xpath(self.FemaleField)
            type.click()
        else:
            return
#################################################################################
    def Signup(self, email="", confirm_email="", password="", display_name="",Date="", gender=""):
        self.ClearEmail()
        self.EnterEmail(email)
        self.ClearConfirmEmail()
        self.EnterConfirmEmail(confirm_email)
        self.ClearPassword()
        self.EnterPassword(password)
        self.ClearDisplayName()
        self.EnterDisplay(display_name)
        #self.EnterDay(day)
        #self.EnterMonth(index_of_month)
        #self.EnterYear(year)
        self.SendDate(Date)
        self.GetAndClickGenderField(gender)
        self.ClickSignupBtn()
    def VerifyLoginSuccessful(self):
        result = self.IsElementPresent("nav-btn",LocatorType="id")
        return result
    def verifyLoginFailed(self):
       result = self.IsElementPresent("nav-btn", LocatorType="id")
       return not result
    def clearFields(self):
        EmailField = self.GetElement(Locator=self.EmailField,LocatorType="xpath")
        EmailField.clear()
        ConfirmEmailField = self.GetElement(Locator=self.ConfirmEmailField,LocatorType="xpath")
        ConfirmEmailField.clear()
        PasswordField = self.GetElement(Locator=self.PasswordField,LocatorType="xpath")
        PasswordField.clear()
        DisplayField = self.GetElement(Locator=self.DisplayField,LocatorType="xpath")
        DisplayField.clear()
        '''DayField = self.GetElement(Locator=self.DayField)
        DayField.clear()
        YearField = self.GetElement(Locator=self.YearField)
        YearField.clear()'''
    def ClearEmail(self):
        EmailField = self.GetElement(Locator=self.EmailField, LocatorType="xpath")
        EmailField.clear()
    def ClearConfirmEmail(self):
        ConfirmEmailField = self.GetElement(Locator=self.ConfirmEmailField, LocatorType="xpath")
        ConfirmEmailField.clear()
    def ClearPassword(self):
        PasswordField = self.GetElement(Locator=self.PasswordField, LocatorType="xpath")
        PasswordField.clear()
    def ClearDisplayName(self):
        DisplayField = self.GetElement(Locator=self.DisplayField, LocatorType="xpath")
        DisplayField.clear()



