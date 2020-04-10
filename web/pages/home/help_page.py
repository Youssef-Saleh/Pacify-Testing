from selenium import webdriver
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
from web.utilities.teststatues import TestStatus
import logging
import web.utilities.custom_logger as cl
import time

class helppage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self,driver):
        self.driver=driver

    #locators
    _help_tap = "Help"
    _search_bar="search"

    _video_tutorial_listen_ofline="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[1]/div/div/a"
    _video_tutorial_spotify_connect = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[2]/div/div/a"
    _video_tutorial_spotify_on_chrome ="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[3]/div/div/a"
    _video_tutorial_make_playlist = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[4]/div/div/a"
    _video_tutorial_search = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[5]/div/div/a"
    ############################
    _listen_offline="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[2]/div/ol/li[1]"
    _spotify_connect="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[2]/div/ol/li[2]"
    spotify_on_chrome="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[2]/div/ol/li[3]"
    _make_playlist="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[2]/div/ol/li[4]"
    _search="/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[2]/div/ol/li[5]"
    _play_search="/html/body/div/div[7]/div[3]/button"


    #####################################################################################
    def click_help_link(self):
        self.elementClick(self._help_tap,locatorType="link")
    def sendkeys_search_bar(self,data):
        self.sendKeys(data,self._search_bar,"id")
    ########################################################################################
    def verify_listen_offline(self):
        result = self.isElementPresent(self._video_tutorial_listen_ofline, locatorType="xpath")
        return result
    def verify_spotify_connect(self):
        result = self.isElementPresent(self._video_tutorial_spotify_connect, locatorType="xpath")
        return result
    def verify_spotify_on_chrome(self):
        result = self.isElementPresent(self._video_tutorial_spotify_on_chrome, locatorType="xpath")
        return result
    def verify_make_playlist(self):
        result = self.isElementPresent(self._video_tutorial_make_playlist, locatorType="xpath")
        return result
    def verify_search(self):
        result = self.isElementPresent(self._video_tutorial_search, locatorType="xpath")
        return result
    ##################################################################
    def click_search_dot(self):
        self.elementClick(self._search,locatorType="xpath")
    def click_make_playlist_dot(self):
        self.elementClick(self._make_playlist,locatorType="xpath")
    def click_spotify_on_chrome_dot(self):
        self.elementClick(self.spotify_on_chrome, locatorType="xpath")
    def click_spotify_connect_dot(self):
        self.elementClick(self._spotify_connect,locatorType="xpath")
    def click_listen_offline_dot(self):
        self.elementClick(self._listen_offline,locatorType="xpath")
    ##################################################################
    def click_search_video(self):
        self.elementClick(self._video_tutorial_search,locatorType="xpath")
    def click_make_playlist(self):
        self.elementClick(self._video_tutorial_make_playlist,locatorType="xpath")
    def click_spotify_on_chrome(self):
        self.elementClick(self._video_tutorial_spotify_on_chrome,locatorType="xpath")
    def click_spotify_connect(self):
        self.elementClick(self._video_tutorial_spotify_connect,locatorType="xpath")
    def click_listen_offline(self):
        self.elementClick(self._listen_offline,locatorType="xpath")
    ##############################################
    def search_video_fn(self):
        time.sleep(1)
        self.click_search_dot()
        self.click_search_video()
    def make_playlist_video_fn(self):
        time.sleep(1)
        self.click_make_playlist_dot()
        self.click_make_playlist()
    def make_spotify_connect_fn(self):
        time.sleep(1)
        self.click_spotify_connect_dot()
        self.click_spotify_connect()
    def make_listen_offline_fn(self):
        time.sleep(1)
        self.click_listen_offline_dot()
        self.click_listen_offline()
    def make_search_fn(self):
        self.click_search_dot()
        self.click_search_video()
     ############################################################################
    def verfication_method(self):
        result1=self.verify_make_playlist()
        result2=self.verify_search()
        result3=self.verify_listen_offline()
        result4=self.verify_spotify_connect()
        result5=self.verify_spotify_on_chrome()
        if result1 is True:
            '''self.ts.markFinal("make playlist",result1,"making playlist is valid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.click_make_playlist()
        elif result2 is True:
            '''self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is valid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.click_search_video()
        elif result3 is True:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is valid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.click_listen_offline()
        elif result4 is True:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is valid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.click_spotify_connect()
        else:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is valid")'''
            self.click_spotify_on_chrome()

        '''result = self.verify_make_playlist()
        if result is not False:
            self.ts.markFinal("spotify_connect_video", result, "spotify connect Valid")
            self.click_make_playlist()
        else:
            self.ts.markFinal("_spotify_connect_video", result, "spotify connect Invalid")'''
