from tests.home.login_test_project import LoginTest
from tests.home.Like_test import LikedListTest
from tests.home.login_test_android import LoginTestAndroid
from tests.home.Edit_test_Android import EditTest
import unittest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(LikedListTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(LoginTestAndroid)
tc4 = unittest.TestLoader().loadTestsFromTestCase(EditTest)
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(smokeTest)