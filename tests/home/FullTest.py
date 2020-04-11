from tests.home.HelpTests import HelpTests
from tests.home.DownloadTests import DownloadTests
from tests.home.PremiumTests import PremiumTests
from tests.home.SignupTests import SignupTests
from tests.home.LoginTests import LoginTests
import unittest

TestSuite1 = unittest.TestLoader().loadTestsFromTestCase(HelpTests)
TestSuite2 = unittest.TestLoader().loadTestsFromTestCase(DownloadTests)
TestSuite3 = unittest.TestLoader().loadTestsFromTestCase(PremiumTests)
TestSuite4 = unittest.TestLoader().loadTestsFromTestCase(SignupTests)
TestSuite5 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
FullTest = unittest.TestSuite([TestSuite1, TestSuite2, TestSuite3, TestSuite4, TestSuite5])
unittest.TextTestRunner(verbosity=2).run(FullTest)
