from selenium import webdriver
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl
import time

class homepage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
    #locators
    _help_tab = "/html/body/div[2]/div[1]/header/div/nav/ul/li[2]/a"
    _download_tab = "Download"
    _signup_tab = "Sign up"
    _premieum_tab = "Premium"
    _Login_tab = "Log In"
    _getsFree_tab = "GET SPOTIFY FREE"
    _help_tab_footer = "/html/body/div[3]/footer/nav/div[2]/dl[3]/dd[1]/a"
    _web_player = "Web Player"
    _free_mobile_app = "Free Mobile App"
    _for_artists = "For Artists"
    _Developers = "Developers"
    _Brands = "Brands"
    _About = "About"
    _For_the_Records = "For the Record"
    _spotify_logo="/html/body/div[2]/div[1]/header/div/div[1]/a/span/svg"

    def click_spotify_logo(self):
        self.elementClick(self._spotify_logo,locatorType="xpath")
    def click_help_link(self):
        self.elementClick(self._help_tab, locatorType="xpath")
    def click_download_tab(self):
        self.elementClick(self._download_tab, locatorType="link")
    def click_signup_tab(self):
        self.elementClick(self._signup_tab, locatorType="link")

    def click_premieum_tab(self):
        self.elementClick(self._premieum_tab, locatorType="link")

    def click_Login_tab(self):
        self.elementClick(self._Login_tab, locatorType="link")

    def click_getsFree_tab(self):
        self.elementClick(self._Login_tab, locatorType="link")

    def click_help_tab_footer(self):
        self.elementClick(self._help_tab_footer, locatorType="xpath")

    def click_web_player(self):
        self.elementClick(self._web_player, locatorType="link")


    def click_for_artists(self):
        self.elementClick(self._for_artists, locatorType="link")

    def click_Developers(self):
        self.elementClick(self._Developers, locatorType="link")

    def click_Brands(self):
        self.elementClick(self._Brands, locatorType="link")

    def click_About(self):
        self.elementClick(self._About, locatorType="link")

    def click_For_the_Records(self):
        self.elementClick(self._For_the_Records, locatorType="link")
###############################################
    def click_footer_functions(self , driver):

        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.click_web_player()
        self.driver.back()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.click_Developers()
        self.driver.back()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.click_Brands()
        self.driver.back()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.click_About()
        self.driver.back()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.click_For_the_Records()
        self.driver.back()
        self.driver.execute_script("window.scrollBy(0, -1000);")

