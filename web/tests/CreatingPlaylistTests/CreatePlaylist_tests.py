from web.pages.home.signup_page import signuppage
from web.base.selenium_driver import SeleniumDriver
from web.base.webdriverfactory import WebDriverFactory
import unittest
from web.utilities.teststatues import TestStatus
import time
from web.pages.CreatePlaylist.CreatePlaylistPage import CreatePlaylist

class Test_F_Playlist(unittest.TestCase, SeleniumDriver):
    wdf=WebDriverFactory("chrome")
    Driver=wdf.GetWebDriverInstance()
    su=signuppage(Driver)
    su.LoginFN("okay9@gmail.com","2222222222")
    cp=CreatePlaylist(Driver)
    ts=TestStatus(Driver)
    def test_A_CreatePlaylist(self):
        self.cp.ClickCreatePlaylist()
        Name=self.cp.NamingPlaylist("sayed")
        self.cp.Create_Playlist()
        time.sleep(0.5)
        self.cp.CancelCreatingPlaylist()
        self.Driver.refresh()
        self.cp.ClickLibrary()
        time.sleep(0.5)
        self.Driver.execute_script("window.scrollBy(0, 10000);")
        self.ts.ScreenShot1("Verifying Making Playlist")
        time.sleep(3)
        self.Driver.quit()
