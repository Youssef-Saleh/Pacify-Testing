from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from web.base.selenium_driver import SeleniumDriver
import unittest
from web.tests.home.signup_incorrect_tests import Test_G_SignupINCorrect
from web.tests.CreatingPlaylistTests.CreatePlaylist_tests import Test_F_Playlist
from web.tests.HomePageTests.CorrectHome_tests import Test_A_HomeCorrect
from web.tests.HomePageTests.home_tests import Test_B_Home
from web.tests.home.signup_correct_tests import Test_C_SignupCorrect
from web.tests.home.Signup_testsF import Test_D_SignupCorrectFacebook
from web.tests.home.signup_fixing_problem import Test_E_SignupFix

tc1 = unittest.TestLoader().loadTestsFromTestCase(Test_A_HomeCorrect)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Test_B_Home)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Test_C_SignupCorrect)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Test_D_SignupCorrectFacebook)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Test_E_SignupFix)
tc6 = unittest.TestLoader().loadTestsFromTestCase(Test_F_Playlist)
tc7 = unittest.TestLoader().loadTestsFromTestCase(Test_G_SignupINCorrect)


# Create a test suite combining TestClass1 and TestClass2
smokeTest = unittest.TestSuite([tc1,tc2,tc3,tc4,tc5,tc6])
unittest.TextTestRunner(verbosity=2).run(smokeTest)