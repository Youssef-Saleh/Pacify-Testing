from web.pages.home.signup_page import signuppage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
from web.base.webdriverfactory import WebDriverFactory
import unittest
from web.utilities.teststatues import TestStatus
from selenium.webdriver import ActionChains
import logging
import time
import web.utilities.custom_logger as cl
from web.pages.CreatePlaylist.CreatePlaylistPage import CreatePlaylist

class Test_stress(unittest.TestCase, SeleniumDriver):
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
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.cp.ClickLibrary()
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        Result=self.cp.VerifyPlaylistMadeSuccesfull(Name)
        self.ts.markFinal("test_MakingPlaylist", Result, "Making playlist done successfully")