from appium import webdriver
import time
from Android.base.appium_driver import AppiumDriver
import logging
import Android.utilities.custom_logger_and as cl

class Library(AppiumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver=driver
    #locators
    #Your LibraryField
    #nav_favorites

    _Login_tab = "login_button"
    EmailField="Email_logIn_text"
    PasswordField="password_login_editText"
    LoginBtn="login_button"
    LibraryField= "com.example.pacify:id/nav_favorites"
    Settings="logout_button"
    Logout="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout"

    def ClickLogin(self):
        self.elementClick(self._Login_tab,"id")
    def SendEmail(self,email):
        self.sendKeys(email,self.EmailField,"id")
    def SendPassword(self,Pass):
        self.sendKeys(Pass,self.PasswordField,"id")
    def submitLogin(self):
        self.elementClick(self.LoginBtn,"id")
    def Login(self,Email,Pass):
        self.ClickLogin()
        time.sleep(0.25)
        self.SendEmail(Email)
        self.SendPassword(Pass)
        self.submitLogin()
    def ClickLibrary(self):
        self.elementClick(self.LibraryField, "id")
    def ClickLogout(self):
        self.elementClick(self.Logout,"xpath")
    def ClickSetting(self):
        self.elementClick(self.Settings,"id")
