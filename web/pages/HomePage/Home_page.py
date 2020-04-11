from selenium import webdriver
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import logging
import web.utilities.custom_logger as cl
import time

class homepage(SeleniumDriver):

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver = Driver
    #locators
    HelpLink = "/html/body/div/div/nav/div/div/a[2]"
    DownloadLink = "Download"
    SignupLink = "Sign-up"
    PremieumLink = "Premium"
    LoginLink = "Login"
    HelpLinkFooter = "/html/body/div/div/div[2]/div[4]/div/a[2]/h4"
    WebPlayer = "/html/body/div/div/div[2]/div[4]/div/a[3]/h4"
    ForArtistsLink = "/html/body/div/div/div[2]/div[3]/div/a[2]/h4"
    AboutLink = "/html/body/div/div/div[2]/div[2]/div/a[2]/h4"
    SpotifyLogo= "/html/body/div[1]/nav/div/a/img"
    Instagram="/html/body/div[3]/footer/div/div/div[4]/a[1]/i"
    Facebook="/html/body/div[3]/footer/div/div/div[4]/a[3]/i"
    Twitter="/html/body/div[3]/footer/div/div/div[4]/a[2]/i"
    SpotifyLogoFooter="/html/body/div[3]/footer/div/div/a/img"
    ForTheRecordsLink = "/html/body/div/div/div[2]/div[2]/div/a[3]/h4"
    FreeMobileAppLink = "/html/body/div/div/div[2]/div[4]/div/a[4]/h4"
    BrandsLink = "/html/body/div/div/div[2]/div[3]/div/a[4]/h4"
    DevelopersLink = "/html/body/div/div/div[2]/div[3]/div/a[3]/h4"
    TryAgainLinkDownload="/html/body/div/div/div/div[1]/div/div[3]/p[1]/u"
    TermsandConditions="Terms and Conditions of Use"
    PrivacyPolicy="Privacy Policy"
    TermsandConditionsLogin = "/html/body/div/div/div[2]/div[4]/form/div[12]/div[1]/p[1]/a "
    PrivacyPolicyLogin = "/html/body/div/div/div[2]/div[8]/div[3]/p/a[2]"
    '''
    GetsFreeLink = "GET SPOTIFY FREE"
    "'''
    def  ClickTermsandConditionsLogin(self):
        self.ElementClick(self.TermsandConditionsLogin,"xpath")
    def ClickPrivacyLogin(self):
        self.ElementClick(self.PrivacyPolicyLogin, "xpath")
    def ClickTermsandConditions(self):
        self.ElementClick(self.TermsandConditions,"link")
    def ClickPrivacy(self):
        self.ElementClick(self.PrivacyPolicy,"link")
    def ClickTryAgain(self):
        self.ElementClick(self.TryAgainLinkDownload,LocatorType="xpath")
    def ClickSpotifyLogo(self):
        self.ElementClick(self.SpotifyLogo, LocatorType="xpath")
    def ClickHelpLink(self):
        self.ElementClick(self.HelpLink, LocatorType="xpath")
    def ClickDownloadLink(self):
        self.ElementClick(self.DownloadLink, LocatorType="link")
    def ClickSignupLink(self):
        self.ElementClick(self.SignupLink, LocatorType="link")
    def ClickPremieumLink(self):
        self.ElementClick(self.PremieumLink, LocatorType="link")
    def clickLoginLink(self):
        self.ElementClick(self.LoginLink, LocatorType="link")
    def ClickGetsFreeLink(self):
        self.ElementClick(self.LoginLink, LocatorType="link")
    def ClickHelpLinkFooter(self):
        self.ElementClick(self.HelpLinkFooter, LocatorType="xpath")
    def ClickWebPlayer(self):
        self.ElementClick(self.WebPlayer, LocatorType="xpath")
    def ClickForArtists(self):
        self.ElementClick(self.ForArtistsLink, LocatorType="xpath")
    def ClickDevelopers(self):
        self.ElementClick(self.DevelopersLink, LocatorType="xpath")
    def ClickBrands(self):
        self.ElementClick(self.BrandsLink, LocatorType="xpath")
    def ClickAbout(self):
        self.ElementClick(self.AboutLink, LocatorType="xpath")
    def ClickForTheRecords(self):
        self.ElementClick(self.ForTheRecordsLink, LocatorType="xpath")
    def ClickTwitter(self):
        self.ElementClick(self.Twitter,LocatorType="xpath")
    def ClickFacebook(self):
        self.ElementClick(self.Facebook,LocatorType="xpath")
    def ClickInstagram(self):
        self.ElementClick(self.Instagram, LocatorType="xpath")
    ###############################################
    def ClickFooterFN(self, Driver):

        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.ClickWebPlayer()
        time.sleep(0.5)
        self.Driver.back()
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.ClickFacebook()
        time.sleep(0.5)
        self.Driver.back()
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.ClickTwitter()
        time.sleep(0.5)
        self.Driver.back()
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.ClickAbout()
        time.sleep(0.5)
        self.Driver.back()
        self.Driver.execute_script("window.scrollBy(0, 1000);")
        self.Instagram()
        time.sleep(0.5)
        self.Driver.back()
        self.Driver.execute_script("window.scrollBy(0, -1000);")

