from selenium import webdriver
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
from web.utilities.teststatues import TestStatus
import logging
import web.utilities.custom_logger as cl
import time

class helppage(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)


    def __init__(self, Driver):
        self.Driver=Driver

    #locators
    HelpLink = "/html/body/div/div/nav/div/div/a[2]"
    #SearchBar= "search"
    ListenOflineVideo="/html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[1]/div/div/a"
    SpotifyConnectVideo ="/html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/a"
    SpotifyOnChromeVideo ="/html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[3]/div/div/a"
    MakePlaylistVideo ="/html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[4]/div/div/a"
    SearchVideo ="/html/body/div/div/div[2]/div/div/div/div[2]/div/div/div[5]/div/div/a"
    ############################
    ListenOflineDot= "/html/body/div/div/div[2]/div/div/div/div[2]/div/ol/li[1]"
    SpotifyConnectDot= "/html/body/div/div/div[2]/div/div/div/div[2]/div/ol/li[2]"
    SpotifyOnChromeDot= "/html/body/div/div/div[2]/div/div/div/div[2]/div/ol/li[3]"
    MakePlaylistDot= "/html/body/div/div/div[2]/div/div/div/div[2]/div/ol/li[4]"
    SearchDot= "/html/body/div/div/div[2]/div/div/div/div[2]/div/ol/li[5]"
    ###################################################################################

    PlayVideo="/html/body/div/div[1]/div[6]/svg[2]"
    PauseVideo="/html/body/div/div[7]/div[3]/button"

    #####################################################################################
    def ClickHelpLink(self):
        self.ElementClick(self.HelpLink, LocatorType="xpath")
    def SendkeysSearchBar(self, data):
        self.SendKeys(data, self.SearchBar, "id")
    ########################################################################################
    def VerifyListenOffline(self):
        result = self.IsElementPresent(self.ListenOflineVideo, LocatorType="xpath")
        return result
    def VerifySpotifyConnect(self):
        result = self.IsElementPresent(self.SpotifyConnectVideo, LocatorType="xpath")
        return result
    def VerifySpotifyOnChrome(self):
        result = self.IsElementPresent(self.SpotifyOnChromeVideo, LocatorType="xpath")
        return result
    def VerifyMakePlaylist(self):
        result = self.IsElementPresent(self.MakePlaylistVideo, LocatorType="xpath")
        return result
    def VerifySearch(self):
        result = self.IsElementPresent(self.SearchVideo, LocatorType="xpath")
        return result
    ##################################################################
    def ClickSearchDot(self):
        self.ElementClick(self.SearchDot, LocatorType="xpath")
    def ClickMakePlaylistDot(self):
        self.ElementClick(self.MakePlaylistDot, LocatorType="xpath")
    def ClickSpotifyOnChromeDot(self):
        self.ElementClick(self.SpotifyOnChromeDot, LocatorType="xpath")
    def ClickSpotifyConnectDot(self):
        self.ElementClick(self.SpotifyConnectDot, LocatorType="xpath")
    def ClickListenOfflineDot(self):
        self.ElementClick(self.ListenOflineDot, LocatorType="xpath")
    ##################################################################
    def ClickSearchVideo(self):
        self.ElementClick(self.SearchVideo, LocatorType="xpath")
    def ClickMakePlaylistVideo(self):
        self.ElementClick(self.MakePlaylistVideo, LocatorType="xpath")
    def ClickSpotifyOnChromeVideo(self):
        self.ElementClick(self.SpotifyOnChromeVideo, LocatorType="xpath")
    def ClickSpotifyConnectVideo(self):
        self.ElementClick(self.SpotifyConnectVideo, LocatorType="xpath")
    def ClickListenOffline(self):
        self.ElementClick(self.ListenOflineDot, LocatorType="xpath")
    def PlayVideo(self):
        self.ElementClick(self.PlayVideo,LocatorType="xpath")
    def PauseVideo(self):
        self.ElementClick(self.PauseVideo,LocatorType="xpath")
    ##############################################
    def MakeSearchFN(self):
        time.sleep(1)
        self.ClickSearchDot()
        time.sleep(0.5)
        ParentHandle=self.Driver.current_window_handle
        handles= self.Driver.window_handles
        self.ClickSearchVideo()
        time.sleep(0.5)
        for handle in handles:
            if handle not in ParentHandle:
                self.Driver.switch_to.window(handle)
                handles = self.Driver.window_handles
                break

        self.PlayVideo()
        time.sleep(0.5)
        '''self.PauseVideo()
        time.sleep(0.5)'''
    def MakePlaylistFN(self):
        time.sleep(1)
        self.ClickMakePlaylistDot()
        self.ClickMakePlaylistVideo()
    def MakeSpotifyConnectFN(self):
        time.sleep(1)
        self.ClickSpotifyConnectDot()
        self.ClickSpotifyConnectVideo()
    def MakeListenOfflineFN(self):
        time.sleep(1)
        self.ClickListenOfflineDot()
        self.ClickListenOffline()
    def MakeSpotifyOnChromeFN(self):
        self.ClickSpotifyOnChromeDot()
        self.ClickSpotifyOnChromeVideo()
     ############################################################################
    def VerficationMethod(self):
        result1=self.VerifyMakePlaylist()
        result2=self.VerifySearch()
        result3=self.VerifyListenOffline()
        result4=self.VerifySpotifyConnect()
        result5=self.VerifySpotifyOnChrome()
        if result1 is True:
            '''self.ts.markFinal("make playlist",result1,"making playlist is valid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.ClickMakePlaylistVideo()
        elif result2 is True:
            '''self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is valid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.ClickSearchVideo()
        elif result3 is True:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is valid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.ClickListenOffline()
        elif result4 is True:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is valid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is invalid")'''
            self.ClickSpotifyConnectVideo()
        else:
            '''self.ts.markFinal("make playlist", result1, "making playlist is invalid")
            self.ts.markFinal("search", result2, "search is invalid")
            self.ts.markFinal("listen offline", result3, "listen offline is invalid")
            self.ts.markFinal("spotify connect", result4, "spotify connect is invalid")
            self.ts.markFinal("spotify on chrome", result5, "spotify on chrome is valid")'''
            self.ClickSpotifyOnChromeVideo()

        '''result = self.VerifyMakePlaylist()
        if result is not False:
            self.ts.markFinal("spotify_connect_video", result, "spotify connect Valid")
            self.ClickMakePlaylistVideo()
        else:
            self.ts.markFinal("_spotify_connect_video", result, "spotify connect Invalid")'''
