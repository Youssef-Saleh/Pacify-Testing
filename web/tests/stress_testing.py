from web.pages.HomePage.Home_page import homepage
from web.pages.home.signup_page import signuppage
from web.pages.home.signup_page_f import signuppage_f
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
import unittest
import time
from web.pages.CreatePlaylist.CreatePlaylistPage import CreatePlaylist
class Test_stress(unittest.TestCase, SeleniumDriver):
    wdf=WebDriverFactory("chrome")
    Driver=wdf.GetWebDriverInstance()
    hp=homepage(Driver)
    suf=signuppage_f(Driver)
    su=signuppage(Driver)
    cp=CreatePlaylist(Driver)

    def test_StressAFN(self):
        '''for x in range(1000):
            self.hp.ClickHelpLink()'''
        for x in range(1000):
            self.hp.ClickHelpLink()
            time.sleep(0.5)
            self.hp.ClickPremieumLink()
            time.sleep(0.5)
    def test_StressBFN(self):
        self.hp.ClickSignupLink()
        for x in range(1000):
            self.su.ClickSignupBtn()

    def test_StressCFN(self):
        self.su.LoginFN("okay9@gmail.com","2222222222")
        self.cp.ClickCreatePlaylist()
        self.cp.NamingPlaylist("sayed")
        for x in range(1000):
            self.cp.Create_Playlist()

    '''def test_StressDFN(self):
        #This for the handle opening in the original spotify
        for x in range(1000):
            self.suf.ClickSignupFacebook()'''
    #it gives me error as i said in the word
    def test_StressEFN(self):
        self.su.LoginFN("okay9@gmail.com", "2222222222")
        for x in range(1000):
            self.cp.ClickCreatePlaylist()
            self.cp.CancelCreatingPlaylist()


