import pytest
from Android.pages.home.Signup_android import signuppage_android
from Android.base.android_driver_factory import WebDriverFactory


@pytest.yield_fixture()
def A_signup_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def A_oneTime_signup_SetUp(request):
    print("Running one time setUp")
    wdf = WebDriverFactory()
    driver = wdf.configuration()
    su=signuppage_android(driver)
    su.click_signup_link()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")