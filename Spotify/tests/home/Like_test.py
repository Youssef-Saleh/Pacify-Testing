import time
from selenium import webdriver
from pages.home.Liked_tracks import LikedPage
import unittest

class LikedListTest(unittest.TestCase):

    def test_all_songs(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.LikedLogin("abdobeatz@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        like.click_Song1()
        time.sleep(4)
        like.click_Song2()
        time.sleep(4)
        like.click_Song3()
        time.sleep(4)
        like.click_Song4()
        time.sleep(4)
        like.click_Song5()
        time.sleep(4)
        like.click_Song6()
        time.sleep(4)
        like.click_Song7()
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song8()
        time.sleep(4)
        like.click_Song9()
        time.sleep(4)
        like.click_Song10()
        time.sleep(4)
        like.click_Song11()
        time.sleep(4)
        like.click_Song12()
        time.sleep(4)
        like.click_Song13()
        time.sleep(4)
        like.click_Song14()
        time.sleep(4)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song15()
        time.sleep(7)
        like.click_Song16()
        time.sleep(7)
        like.click_Song17()
        time.sleep(5)
        like.click_Song18()
        time.sleep(5)
        like.click_Song19()
        time.sleep(5)
        like.click_Song20()
        time.sleep(5)
        like.click_Song21()
        time.sleep(5)
        like.click_Song22()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song23()
        time.sleep(5)
        like.click_Song24()
        time.sleep(5)
        like.click_Song25()
        time.sleep(5)
        like.click_Song26()
        time.sleep(5)
        like.click_Song27()
        time.sleep(5)
        like.click_Song28()
        time.sleep(5)
        like.click_Song29()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song30()
        time.sleep(5)
        like.click_Song31()
        time.sleep(5)
        like.click_Song32()
        time.sleep(5)
        like.click_Song33()
        time.sleep(5)
        like.click_Song34()
        time.sleep(5)
        like.click_Song35()
        time.sleep(5)
        like.click_Song36()
        time.sleep(5)
        like.click_Song37()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song38()
        time.sleep(5)
        like.click_Song39()
        time.sleep(5)
        like.click_Song40()
        time.sleep(5)
        like.click_Song41()
        time.sleep(5)
        like.click_Song42()
        time.sleep(5)
        driver.execute_script("window.scrollBy(0, 500);")
        like.click_Song43()
        time.sleep(5)
        like.click_Song44()
        time.sleep(5)
        like.click_Song45()
        time.sleep(5)

    def test_play_pause(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.LikedLogin("abdobeatz@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        like.click_Song1() #play song
        time.sleep(5)
        like.click_Song2()  # play song
        time.sleep(5)
        like.click_Song1() #play song
        time.sleep(5)
        like.click_Song2() #play song
        time.sleep(5)
        like.click_Song1()
        time.sleep(3)
        like.click_Song1() #it should pause here but it return it self
        time.sleep(5)
        like.ClickBarbutton()
        time.sleep(3)
        like.ClickBarbutton()
        time.sleep(3)
        like.click_Song1()

    def test_play_pause_2(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.LikedLogin("abdobeatz@artist.pacify", "Dehkmodhek2")
        time.sleep(5)
        like.click_Song1()  # play song
        time.sleep(5)
        like.click_Song2()
        like.click_Song3()
        like.click_Song4()
        like.click_Song5()
        like.click_Song6()
        time.sleep(5)

    def test_stress3(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.Stress3("abdobeatz@artist.pacify", "Dehkmodhek2")

    def test_stress2(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.Stress2("abdobeatz@artist.pacify", "Dehkmodhek2")

    def test_stress1(self):
        driver = webdriver.Chrome(
            executable_path="C:\\Users\\Mohamed Gaber\\Desktop\\SeleniumWebDriver\\chromedriver_win32\\chromedriver.exe")
        driver.get("http://23.96.41.241/")
        driver.maximize_window()
        driver.implicitly_wait(5)
        like = LikedPage(driver)
        like.Stress1("abdobeatz@artist.pacify", "Dehkmodhek2")











