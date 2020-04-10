
import traceback
from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser


    def getWebDriverInstance(self):

        baseURL = "https://www.spotify.com/uk/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\IEDriverServer.exe")
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\ geckodriver.exe")
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\chromedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path="C:\\Users\\Eslam\\PycharmProjects\\web\\drivers\\chromedriver.exe")
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)

        return driver

