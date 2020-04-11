from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time
from selenium.webdriver.common.keys import Keys

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver

    #Locators
    LoginLink = "Login" #link text
    EmailField = "email" #name
    PasswordField = "password" #name
    LoginButton = "/html/body/div/div/div[2]/div[5]/form/div[5]/button" #xpath
    FacebookButton= "/html/body/div/div/div[2]/div[2]/div/a"  #xpath
    FacebookUsername= "email"
    FacebookPassword= "pass"
    FacebookLogin= "loginbutton"
    ForgetpasswordButton = "/html/body/div/div/div[2]/div[6]/a/a" # link
    ForgetEmail= "email" #name
    Send = "/html/body/div/form/div/div[4]/button" #xpath
    RememberMe = "checked" #name
    SignupButton = "SIGN UP FOR SPOTIFY" #
    Logo = "/html/body/div/div/div[1]/a/h1"
    Apple = "/html/body/div/div/div[2]/div[3]/div/a"
    Terms = "/html/body/div/div/div[2]/div[8]/div[3]/p/a[1]"
    Privacy = "/html/body/div/div/div[2]/div[8]/div[3]/p/a[2]"



    def EnterEmail(self, email):
         self.SendKeys(email, self.EmailField, "name")

    def EnterPassword(self, password):
         self.SendKeys(password, self.PasswordField, "name")

    def EnterFacebookUsername(self, email):
        self.SendKeys(email, self.FacebookUsername)

    def EnterFacebookPassword(self, password):
        self.SendKeys(password, self.FacebookPassword)

    def EnterForgetEmail(self, email):
        self.SendKeys(email, self.ForgetEmail, "name")

    def ClickLoginButton(self):
         self.ElementClick(self.LoginButton, "xpath")

    def ClickLoginLink(self):
         self.ElementClick(self.LoginLink, "link")

    def ClickTerms(self):
         self.ElementClick(self.Terms, "link")

    def ClickPrivacy(self):
         self.ElementClick(self.Privacy, "link")


    def ClickFacebookButton(self):
        self.ElementClick(self.FacebookButton, "xpath")

    def ClickFacebookToLogin(self):
        self.ElementClick(self.FacebookLogin)


    def ClickForgetPasswordButton(self):
        self.ElementClick(self.ForgetpasswordButton, "xpath")

    def ClickSend(self):
        self.ElementClick(self.Send, "xpath")

    def ClickRemember(self):
        self.ElementClick(self.RememberMe, "name")

    def ClickSignupbutton(self):
        self.ElementClick(self.SignupButton, "link")


    def ClickSpotify(self):
        self.ElementClick(self.Logo, "xpath")

    def ClickApple(self):
        self.ElementClick(self.Apple, "xpath")

    def ClearPassword(self):
        self.Clears(self.PasswordField, "name")

    def ClearEmail(self):
        self.Clears(self.EmailField, "name")

    def ClearForgetEmail(self):
        self.Clears(self.ForgetEmail, "name")


    def HomeLoginS(self, username, password):
        self.ClickLoginLink()
        time.sleep(2)
        self.ClickSignupbutton()
        time.sleep(5)
        self.driver.back()
        self.driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()

    def HomeLogin(self, username, password):
        self.ClickLoginLink()
        time.sleep(2)
        self.driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()

    def Login(self, username, password):
        time.sleep(2)
        self.ClearEmail()
        self.EnterEmail(username)
        self.ClearPassword()
        self.EnterPassword(password)
        self.ClickLoginButton()
    def LoginWithRemember(self, username, password):
        self.ClickLoginLink()
        time.sleep(2)
        self.driver.implicitly_wait(5)
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickRemember()
        self.ClickLoginButton()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.ClickLoginLink()

    def LoginFacebook(self, username, password):
        self.ClickLoginLink()
        time.sleep(2)
        self.ClickFacebookButton()
        self.EnterFacebookUsername(username)
        self.EnterFacebookPassword(password)
        self.ClickFacebookToLogin()

    def ForgetPassword(self, email):
        # self.driver.back()
        self.ClickLoginLink()
        time.sleep(2)
        self.ClickForgetPasswordButton()
        self.ClickSend()

        self.EnterForgetEmail("ahmed@yahoo.commmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm"
                              "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm")
        self.ClickSend()
        time.sleep(2)
        self.ClearForgetEmail()
        self.EnterForgetEmail(email)
        self.ClickSend()

    def StressLogin1(self):
        self.WaitForElement(self.LoginLink, "xpath")
        self.ClickLoginLink()
        self.driver.implicitly_wait(5)
        i=0
        while(i<1000):
          self.EnterEmail("z")
          i=i+1
        self.EnterPassword("3333333333")
        self.ClickLoginButton()

    def StressLogin2(self):
        self.ClickLoginLink()
        self.driver.implicitly_wait(5)
        self.EnterEmail("modyseka@gmail.com")
        i = 0
        while (i < 1000):
            self.EnterPassword("3")
            i = i + 1
        self.ClickLoginButton()

    def StressLogin3(self):
        self.ClickLoginLink()
        self.driver.implicitly_wait(5)
        i = 0
        while (i < 5000):
            self.EnterPassword("3")
            self.EnterEmail("z")
            i = i + 1
        self.ClickLoginButton()

    def StressLogin4(self):
        self.ClickLoginLink()
        self.driver.implicitly_wait(5)
        self.EnterPassword("3")
        self.EnterEmail("z")
        i = 0
        while (i < 1000):
          self.ClickLoginButton()
          i = i + 1

    def TestApple(self):
        self.ClickLoginLink()
        time.sleep(1)
        self.ClickApple()
        self.driver.back()
        # self.driver.execute_script("window.scrollBy(0, 1000);")
        # time.sleep(3)
        # self.click_terms()
        # elem =self.driver.find_elements_by_tag_name("body")
        # elem.send_keys(Keys.CONTROL + "w")
        # time.sleep(3)
        # self.click_Privacy()
        # elem =self.driver.find_elements_by_tag_name("body")
        # elem.send_keys(Keys.CONTROL + "w")

    def StressLogin5(self):
        self.ClickLoginLink()
        self.driver.implicitly_wait(5)
        i = 0
        while (i < 1000):
          self.EnterPassword("3")
          self.EnterEmail("z")
          self.ClickLoginButton()
          i = i + 1
