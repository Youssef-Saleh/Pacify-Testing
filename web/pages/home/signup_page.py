from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl

class signuppage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver
    #locators
    _signup_link="Sign up"
    _email_field="register-email"
    _confirm_email_field="register-confirm-email"
    _password_field="register-password"
    _display_field="register-displayname"
    _day_field="register-dob-day"
    _month_field="register-dob-month"
    _year_field="register-dob-year"
    _male_field="register-male"
    _female_field="register-female"
    _signup_btn="register-button-email-submit"
    _spotify_logo="/html/body/div[2]/div[2]/div[1]/div/div/a"



    ######################################################################

    def click_spotify_logo(self):
        self.elementClick(self._spotify_logo,"xpath")
    def click_signup_link(self):
        self.elementClick(self._signup_link,locatorType="link")
    def enter_email(self,email):
        self.sendKeys(email,self._email_field)
    def enter_confirm_email(self,confirm_email):
        self.sendKeys(confirm_email,self._confirm_email_field)
    def enter_password(self,password):
        self.sendKeys(password,self._password_field)
    def enter_display(self,display):
        self.sendKeys(display,self._display_field)
    def enter_day(self,day):
        self.sendKeys(day,self._day_field)
    def enter_year(self,year):
        self.sendKeys(year,self._year_field)
    def click_signup_btn(self):
        self.elementClick(self._signup_btn,locatorType="id")

###########################################################
    def get_month_field(self):
        return self.driver.find_element_by_id(self._month_field)
    def enter_month(self,month):
        se=Select(self.get_month_field())
        se.select_by_index(month)
###########################################################
    def get_and_click_gender_field(self, gender):
        if gender == "male" or "Male":
            type = self.driver.find_element_by_id(self._male_field)
            type.click()
        elif gender == "Female" or "female":
            type = self.driver.find_element_by_id(self._female_field)
            type.click()
        else:
            return
#################################################################################
    def signup(self, email="",confirm_email="", password="",display_name="",day="",index_of_month="",year="",gender=""):
        self.clearFields()
        self.enter_email(email)
        self.enter_confirm_email(confirm_email)
        self.enter_password(password)
        self.enter_display(display_name)
        self.enter_day(day)
        self.enter_month(index_of_month)
        self.enter_year(year)
        self.get_and_click_gender_field(gender)
        self.click_signup_btn()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("svelte-kdyqkb",
                                       locatorType="class")
        return result

    def verifyLoginFailed(self):
       result = self.isElementPresent("has-error",locatorType="class")

       return result

    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        confirmEmailField = self.getElement(locator=self._confirm_email_field)
        confirmEmailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()
        displayField = self.getElement(locator=self._display_field)
        displayField.clear()
        dayField = self.getElement(locator=self._day_field)
        dayField.clear()
        yearField = self.getElement(locator=self._year_field)
        yearField.clear()

