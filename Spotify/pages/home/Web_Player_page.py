from base.selenium_driver import SeleniumDriver


class Web_Player(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Locators
    Loginlink = "Log In"
    emailfield = "login-username"
    passwordfield = "login-password" #link
    loginbutton = "login-button"
    Spotify = "svelte-1gcdbl9" #class
    web_player_button = "segmented-desktop-launch"
    buttonbar = "/html/body/div[3]/div/div[3]/div[3]/footer/div/div[2]/div/div[1]/div[3]/button"

    def entereamil(self, email):
         self.SendKeys(email, self.emailfield)

    def enterpassword(self, password):
         self.SendKeys(password, self.passwordfield)

    def clickloginlink(self):
         self.ElementClick(self.Loginlink, "link")

    def clickloginbutton(self):
         self.ElementClick(self.loginbutton)

    def click_on_spotify(self):
         self.ElementClick(self.Spotify, "class")

    def click_on_web_player(self):
         self.ElementClick(self.web_player_button)



    def Login_webplayer(self, username, password):
        self.clickloginlink()
        self.entereamil(username)
        self.enterpassword(password)
        self.clickloginbutton()
        self.click_on_spotify()
        self.click_on_web_player()

    def click_on_song(self,song,button):
        self.click_song(song, "xpath", button)

    def click_on_bar(self):
        self.ElementClick(self.buttonbar, "xpath")

