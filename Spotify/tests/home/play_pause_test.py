import time
from selenium import webdriver
from pages.home.Web_Player_page import Web_Player
import unittest
song31 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[3]/section/div/div[2]/div/div/div[3]"
button31 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[3]/section/div/div[2]/div/div/div[3]/button"
song32 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[3]/section/div/div[3]/div/div/div[3]"
button32 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[3]/section/div/div[3]/div/div/div[3]/button"
button_stop_recent = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[1]/section/div/div[2]/div/div/div[3]/button"
song11 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[1]/section/div/div[2]/div/div/div[3]"
song41 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[2]/div/div/div[3]"
button41 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[2]/div/div/div[3]/button"
song42 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[3]/div/div/div[3]"
button42 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[3]/div/div/div[3]/button"
song43 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[4]/div/div/div[3]"
button43= "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[4]/div/div/div[3]/button"
song44 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[5]/div/div/div[3]"
button44 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[5]/div/div/div[3]/button"
song45 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[6]/div/div/div[3]"
button45 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[6]/div/div/div[3]/button"
song46 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[7]/div/div/div[3]"
button46 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[4]/section/div/div[7]/div/div/div[3]/button"
song23 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[2]/section/div/div[4]/div/div/div[3]"
button23 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[2]/section/div/div[4]/div/div/div[3]/button"
song13 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[1]/section/div/div[4]/div/div/div[3]"
button13 = "/html/body/div[3]/div/div[3]/div[4]/div[1]/div/div[2]/section/section/div[1]/section/div/div[4]/div/div/div[3]/button"
class UserActions():
    def test_songs(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.spotify.com/eg-en//")
        driver.maximize_window()
        driver.implicitly_wait(5)
        pp = Web_Player(driver)
        pp.Login_webplayer("modyseka@gmail.com", "3333333333")

        pp.click_on_song(song32, button32)
        time.sleep(8) #play
        pp.click_on_song(song31, button31)
        time.sleep(8) #play
        pp.click_on_song(song32, button32)
        time.sleep(8) #play
        pp.click_on_song(song31, button31)
        time.sleep(8) #play
        pp.click_on_song(song31, button31)
        time.sleep(5) #stop
        pp.click_on_bar()
        time.sleep(8) #play
        pp.click_on_song(song11, button_stop_recent)
        time.sleep(5)  # stop from recent
        pp.click_on_song(song41, button41)
        time.sleep(8) #play
        pp.click_on_song(song42, button42)
        time.sleep(8) #play
        pp.click_on_bar()
        time.sleep(5) #stop from bar
        pp.click_on_bar()
        time.sleep(5) #play from bar
        pp.click_on_song(song43, button43)
        time.sleep(8) #play
        pp.click_on_song(song44, button44)
        time.sleep(8) #play
        pp.click_on_song(song45, button45)
        time.sleep(8)  # play
        pp.click_on_song(song11, button_stop_recent)
        time.sleep(5)  # stop from recent
        pp.click_on_song(song11, button_stop_recent)
        time.sleep(8)   # play from recent
        pp.click_on_song(song46, button46)
        time.sleep(8)  # play from recent
        pp.click_on_song(song23, button23)
        time.sleep(8) #play
        pp.click_on_song(song23, button23)
        time.sleep(5) #stop
        pp.click_on_song(song13, button13)
        time.sleep(8)  # play
        pp.click_on_song(song11, button_stop_recent)
        time.sleep(5) #stop



f=UserActions()
f.test_songs()
