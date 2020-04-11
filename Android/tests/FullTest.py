import unittest
from Android.tests.home.Library_tests import Library_test
from Android.tests.home.home_tests import home_test
from Android.tests.home.And_signup_tests import signup_android_test

tc1 = unittest.TestLoader().loadTestsFromTestCase(Library_test)
tc2 = unittest.TestLoader().loadTestsFromTestCase(home_test)
tc3 = unittest.TestLoader().loadTestsFromTestCase(signup_android_test)
smokeTest = unittest.TestSuite([tc1])
unittest.TextTestRunner(verbosity=2).run(smokeTest)