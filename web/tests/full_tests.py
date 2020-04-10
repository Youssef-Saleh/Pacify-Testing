from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.pages.home.signup_page import signuppage
from web.pages.home.signup_page_f import signuppage_f
from web.tests import conftest
from web.base.selenium_driver import SeleniumDriver
import unittest
from web.tests.home.signup_tests import Testsignup
from web.tests.home.home_tests import Test_home

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_home)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Testsignup)
# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)