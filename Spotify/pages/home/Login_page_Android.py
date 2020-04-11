from base.appium_driver import AppiumDriver
import time

class LoginPage(AppiumDriver):
    def __init__(self ,driver):
        super().__init__(driver)
        self.driver =driver

    #Locators
    LoginLink = "com.example.pacify:id/login_button"
    EmailField = "com.example.pacify:id/Email_logIn_text"
    PasswordField = "com.example.pacify:id/password_login_editText"
    ShowPassword = "com.example.pacify:id/text_input_end_icon"
    LoginButton = "com.example.pacify:id/login_button"
    FacebookButton = "com.example.pacify:id/facebookLogin_button"
    FacebookUsername = "email"
    FacebookPassword = "pass"
    FacebookLogin = "loginbutton"
    Settings = "com.example.pacify:id/logout_button"
    YourLibrary = "com.example.pacify:id/nav_favorites"
    Logout = "android:id/summary"

    ForgetPasswordButton = "com.example.pacify:id/login_forget_password_button"
    ForgetEmail = "com.example.pacify:id/Email_ForgetPass_text"
    GetLink = "com.example.pacify:id/GetLink_button"

    SignupButton = "sign-up-link"
    Logo = "spotify-logo"

    def EnterEmail(self, email):
         self.sendKeys(email, self.EmailField)

    def EnterPassword(self, password):
         self.sendKeys(password, self.PasswordField)

    def EnterFacebookUsername(self, email):
        self.sendKeys(email, self.FacebookUsername)

    def EnterFacebookPassword(self, password):
        self.sendKeys(password, self.FacebookPassword)

    def EnterForgetEmail(self, email):
        self.sendKeys(email, self.ForgetEmail)

    def ClickLoginButton(self):
         self.elementClick(self.LoginButton)

    def ClickLoginLink(self):
         self.elementClick(self.LoginLink)

    def ClickShowPassword(self):
         self.elementClick(self.ShowPassword)

    def ClickLibrary(self):
        self.elementClick(self.YourLibrary)

    def ClickSettings(self):
        self.elementClick(self.Settings)

    def ClickGetLink(self):
        self.elementClick(self.GetLink)

    # def ClickFacebookLogin(self):
    #     self.elementClick(self.FacebookButton, "id")
    #
    # def clickfacebooktologin(self):
    #     self.elementClick(self.FacebookLogin)

    def clicklogout(self):
        self.elementClick(self.Logout)

    def ClickForgetPasswordButton(self):
        self.elementClick(self.ForgetPasswordButton)

    def ClickSend(self):
        self.elementClick(self.GetLink)


    def clearpassword(self):
        self.clears(self.PasswordField)

    def clearemail(self):
        self.clears(self.EmailField)

    def clear_forget_email(self):
        self.clears(self.ForgetEmail)

    def Homelogin(self, username, password):
        self.ClickLoginLink()
        self.driver.implicitly_wait(2)
        self.EnterEmail(username)
        self.EnterPassword(password)

    def login(self, username, password):
        self.clearemail()
        self.clearpassword()
        self.EnterEmail(username)
        self.EnterPassword(password)

    def final_login(self, username, password):
        self.clearemail()
        self.clearpassword()
        self.EnterEmail(username)
        self.EnterPassword(password)
        self.ClickLoginButton()

    def log_out(self):
        self.ClickLibrary()
        self.ClickSettings()
        self.clicklogout()


    def forgetpassword(self, email):
        self.ClickLoginLink()
        time.sleep(2)
        self.ClickForgetPasswordButton()
        time.sleep(3)
        self.EnterForgetEmail(email)

