import pytest
from selenium import webdriver
from web.base.webdriverfactory import WebDriverFactory
from web.pages.home.signup_page import signuppage
from web.pages.home.Home_page import homepage

#########################################################################################
@pytest.yield_fixture()
def signup_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTime_signup_SetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    su=signuppage(driver)
    su.click_signup_link()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
##############################################################################################
@pytest.yield_fixture(scope="class")
def oneTime_home_SetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")
@pytest.yield_fixture()
def home_setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")
##########################################################################################
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")