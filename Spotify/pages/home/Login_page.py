from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver

    #Locators
    Loginlink = "Log In"
    emailfield = "login-username"
    passwordfield = "login-password"
    loginbutton = "login-button"
    facebookbutton="btn-facebook"
    facebookusername="email"
    facebookpassword="pass"
    facebooklogin="loginbutton"
    menu="svelte-kdyqkb"
    logout="Log Out"
    forgetpasswordbutton="reset-password-link"
    forgetemail="form_input"
    send = "form_send"
    Remember_me = "control-indicator"
    SignUpbutton = "sign-up-link"
    logo = "spotify-logo"
    tohome = "svelte-1gcdbl9"


    def entereamil(self,email):
         self.SendKeys(email, self.emailfield)

    def enterpassword(self,password):
         self.SendKeys(password, self.passwordfield)

    def enterfacebookusername(self, email):
        self.SendKeys(email, self.facebookusername)

    def enterfacebookpassword(self, password):
        self.SendKeys(password, self.facebookpassword)

    def enterforgetemail(self,email):
        self.SendKeys(email, self.forgetemail)

    def clickloginbutton(self):
         self.ElementClick(self.loginbutton)

    def clickloginlink(self):
         self.ElementClick(self.Loginlink, "link")

    def clickmenu(self):
        self.ElementClick(self.menu, "class")

    def clickfacebooklogin(self):
        self.ElementClick(self.facebookbutton, "class")

    def clickfacebooktologin(self):
        self.ElementClick(self.facebooklogin)

    def clicklogout(self):
        self.ElementClick(self.logout, "link")

    def clickforgetpasswordbutton(self):
        self.ElementClick(self.forgetpasswordbutton)

    def clicksend(self):
        self.ElementClick(self.send)

    def clickremember(self):
        self.ElementClick(self.Remember_me, "class")

    def clicksignupbutton(self):
        self.ElementClick(self.SignUpbutton)

    def clickspotify(self):
        self.ElementClick(self.logo, "class")

    def clickstohome(self):
        self.ElementClick(self.tohome, "class")

    def clearpassword(self):
        self.Clears(self.passwordfield)

    def clearemail(self):
        self.Clears(self.emailfield)

    def clear_forget_email(self):
        self.Clears(self.forgetemail)


    def Homelogin(self,username,password):
        self.clickloginlink()
        self.clicksignupbutton()
        self.driver.implicitly_wait(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.entereamil(username)
        self.enterpassword(password)
        self.clickloginbutton()

    def login(self, username, password):
        self.clearemail()
        self.clearpassword()
        self.entereamil(username)
        self.enterpassword(password)
        self.clickloginbutton()
        time.sleep(1)
    def loginwithoutremember(self, password):
        self.clickmenu()
        self.clicklogout()
        self.clickloginlink()
        self.enterpassword(password)
        self.clickremember()
        time.sleep(1)
        self.clickloginbutton()

    def login_facebook(self, username, password):
        self.clickmenu()
        self.clicklogout()
        self.clickloginlink()
        time.sleep(1)
        self.clickfacebooklogin()
        self.enterfacebookusername(username)
        self.enterfacebookpassword(password)
        self.clickfacebooktologin()

    def forgetpassword(self, email):
        self.clickmenu()
        self.clicklogout()
        self.clickloginlink()
        time.sleep(2)
        self.clickforgetpasswordbutton()
        self.clicksend()
        self.enterforgetemail("ahmed@yahoo.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
                              "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        self.clicksend()
        time.sleep(2)
        self.clear_forget_email()
        self.enterforgetemail(email)
        self.clicksend()
        self.clickstohome()

    def stress_login1(self):
        self.clickloginlink()
        self.driver.implicitly_wait(5)
        i=0
        while(i<10000):
          self.entereamil("z")
          i=i+1
        self.enterpassword("3333333333")
        self.clickloginbutton()

    def stress_login2(self):
        self.clickloginlink()
        self.driver.implicitly_wait(5)
        self.entereamil("modyseka@gmail.com")
        i = 0
        while (i < 1000):
            self.enterpassword("33")
            i = i + 1
        self.clickloginbutton()

    def stress_login3(self):
        self.clickloginlink()
        self.driver.implicitly_wait(5)
        i = 0
        while (i < 5000):
            self.enterpassword("3")
            self.entereamil("z")
            i = i + 1
        self.clickloginbutton()

    def stress_login4(self):
        self.clickloginlink()
        self.driver.implicitly_wait(5)
        self.enterpassword("3")
        self.entereamil("z")
        i = 0
        while (i < 10000):
          self.clickloginbutton()
          i = i + 1
    def stress_login5(self):
        self.clickloginlink()
        self.driver.implicitly_wait(5)
        i = 0
        while (i < 1000):
         self.clickloginbutton()
         self.clickspotify()
         i = i + 1
