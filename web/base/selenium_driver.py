from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import web.utilities.custom_logger as cl
import os
import time
import logging

class SeleniumDriver():

    Log = cl.customLogger(logging.DEBUG)

    def __init__(self, Driver):
        self.Driver = Driver

    def ScreenShot1(self, ResultMessage):
        """
        Takes screenshot of the current open web page
        """
        FileName = ResultMessage + "." + str(round(time.time() * 1000)) + ".png"
        ScreenshotDirectory = "../screenshots/"
        RelativeFileName = ScreenshotDirectory + FileName
        CurrentDirectory = os.path.dirname(__file__)
        DestinationFile = os.path.join(CurrentDirectory, RelativeFileName)
        DestinationDirectory = os.path.join(CurrentDirectory, ScreenshotDirectory)

        try:
            if not os.path.exists(DestinationDirectory):
                os.makedirs(DestinationDirectory)
            self.Driver.save_screenshot(DestinationFile)
            self.Log.info("Screenshot save to directory: " + DestinationFile)
        except:
            self.Log.error("### Exception Occurred when taking screenshot")

    def ScreenShot(self, ResultMessage):
        """
        Takes screenshot of the current open web page
        """
        FileName = ResultMessage + "." + str(round(time.time() * 1000)) + ".png"
        ScreenshotDirectory = "../screenshots/"
        RelativeFileName = ScreenshotDirectory + FileName
        CurrentDirectory = os.path.dirname(__file__)
        DestinationFile = os.path.join(CurrentDirectory, RelativeFileName)
        DestinationDirectory = os.path.join(CurrentDirectory, ScreenshotDirectory)

        try:
            if not os.path.exists(DestinationDirectory):
                os.makedirs(DestinationDirectory)
            self.Driver.save_screenshot(DestinationFile)
            self.Log.info("Screenshot save to directory: " + DestinationFile)
        except:
            self.Log.error("### Exception Occurred when taking screenshot")
        print_stack()


    def GetByType(self, LocatorType):
        LocatorType = LocatorType.lower()
        if LocatorType == "id":
            return By.ID
        elif LocatorType == "name":
            return By.NAME
        elif LocatorType == "xpath":
            return By.XPATH
        elif LocatorType == "css":
            return By.CSS_SELECTOR
        elif LocatorType == "class":
            return By.CLASS_NAME
        elif LocatorType == "link":
            return By.LINK_TEXT
        else:
            self.Log.info("Locator type " + LocatorType +
                          " not correct/supported")
        return False

    def GetElement(self, Locator, LocatorType="id"):
        Element = None
        try:
            LocatorType = LocatorType.lower()
            byType = self.GetByType(LocatorType)
            Element = self.Driver.find_element(byType, Locator)
            self.Log.info("Element found with Locator: " + Locator +
                          " and  LocatorType: " + LocatorType)
        except:
            self.Log.info("Element not found with Locator: " + Locator +
                          " and  LocatorType: " + LocatorType)
        return Element

    def ElementClick(self, Locator, LocatorType="id"):
        try:
            Element = self.GetElement(Locator, LocatorType)
            Element.click()
            self.Log.info("Clicked on element with Locator: " + Locator +
                          " LocatorType: " + LocatorType)
        except:
            self.Log.info("Cannot click on the element with Locator: " + Locator +
                          " LocatorType: " + LocatorType)
            print_stack()

    def SendKeys(self, Data, Locator, LocatorType="id"):
        try:
            Element = self.GetElement(Locator, LocatorType)
            Element.send_keys(Data)
            self.Log.info("Sent Data on element with Locator: " + Locator +
                          " LocatorType: " + LocatorType)
        except:
            self.Log.info("Cannot send Data on the element with Locator: " + Locator +
                  " LocatorType: " + LocatorType)
            print_stack()

    def IsElementPresent(self, Locator, LocatorType="id"):
        try:
            Element = self.GetElement(Locator, LocatorType)
            if Element is not None:
                self.Log.info("Element Found")
                return True
            else:
                self.Log.info("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def ElementPresenceCheck(self, Locator, ByType):
        try:
            ElementList = self.Driver.find_elements(ByType, Locator)
            if len(ElementList) > 0:
                self.Log.info("Element Found")
                return True
            else:
                self.Log.info("Element not found")
                return False
        except:
            self.Log.info("Element not found")
            return False

    def WaitForElement(self, Locator, LocatorType="id",
                       Timeout=10, pollFrequency=0.5):
        Element = None
        try:
            ByType = self.GetByType(LocatorType)
            self.Log.info("Waiting for maximum :: " + str(Timeout) +
                  " :: seconds for element to be clickable")
            Wait = WebDriverWait(self.Driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            Element = Wait.until(EC.element_to_be_clickable((ByType,
                                                             "stopFilter_stops-0")))
            self.Log.info("Element appeared on the web page")
        except:
            self.Log.info("Element not appeared on the web page")
            print_stack()
        return Element

    def clears(self, Locator, LocatorType="id"):
        try:
            element = self.GetElement(Locator, LocatorType)
            element.clear()
            print("claer data from element with locator: " + Locator + " locatorType: " + LocatorType)
        except:
            print("Cannot claer data from the element with locator: " + Locator +
                  " locatorType: " + LocatorType)
            print_stack()
