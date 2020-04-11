from selenium import webdriver
from pages.home.HelpPage import HelpPage
import unittest


class HelpTests(unittest.TestCase):
    def setUp(self):
        baseURL = "http://pacify.tech/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.driver.switch_to.frame(0)

    def test_LoadHelpPage(self):
        driver = self.driver
        HP = HelpPage(driver)

        HP.LoadHelpPage()
        SearchBar = HP.verifyHelpPageLoaded()
        self.assertIsNotNone(SearchBar, msg="Help Page not loaded")

    def test_ClickWatchButtonInFirstCarouselItem(self):
        driver = self.driver
        HP = HelpPage(driver)
        HP.LoadHelpPage()
        HP.clickFirstCarouselItem()

        HP.clickWatchButton()
        Player = HP.verifyWatchButtonClicked()
        self.assertIsNotNone(Player, msg="Player not loaded")

    def test_ClickWatchButtonInSecondCarouselItem(self):
        driver = self.driver
        HP = HelpPage(driver)
        HP.LoadHelpPage()
        HP.clickSecondCarouselItem()

        HP.clickWatchButton()
        Player = HP.verifyWatchButtonClicked()
        self.assertIsNotNone(Player, msg="Player not loaded")

    def test_ClickWatchButtonInThirdCarouselItem(self):
        driver = self.driver
        HP = HelpPage(driver)
        HP.LoadHelpPage()
        HP.clickThirdCarouselItem()

        HP.clickWatchButton()
        Player = HP.verifyWatchButtonClicked()
        self.assertIsNotNone(Player, msg="Player not loaded")

    def test_ClickWatchButtonInFourthCarouselItem(self):
        driver = self.driver
        HP = HelpPage(driver)
        HP.LoadHelpPage()
        HP.clickFourthCarouselItem()

        HP.clickWatchButton()
        Player = HP.verifyWatchButtonClicked()
        self.assertIsNotNone(Player, msg="Player not loaded")

    def test_ClickWatchButtonInFifthCarouselItem(self):
        driver = self.driver
        HP = HelpPage(driver)
        HP.LoadHelpPage()
        HP.clickFifthCarouselItem()

        HP.clickWatchButton()
        Player = HP.verifyWatchButtonClicked()
        self.assertIsNotNone(Player, msg="Player not loaded")

    def tearDown(self):
        self.driver.quit()
