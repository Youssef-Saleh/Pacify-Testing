from selenium import webdriver
#from web.tests import conftest
from web.base.webdriverfactory import WebDriverFactory
from web.base.selenium_driver import SeleniumDriver
from web.pages.home.help_page import helppage
import time
import unittest


class Testhelp(unittest.TestCase, SeleniumDriver):

    _video_tutorial_listen_ofline = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[1]/div/div/a"
    _video_tutorial_spotify_connect = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[2]/div/div/a"
    _video_tutorial_spotify_on_chrome = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[3]/div/div/a"
    _video_tutorial_make_playlist = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[4]/div/div/a"
    _video_tutorial_search = "/html/body/div[1]/div/div[6]/div/div/div[2]/div/div[1]/div[5]/div/div/a"
    wdf = WebDriverFactory("chrome")
    driver = wdf.getWebDriverInstance()
    hp=helppage(driver)
    hp.click_help_link()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, 1500);")
    hp.search_video_fn()