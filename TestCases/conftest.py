import pytest

from selenium import webdriver
def pytest_addoption(parser):
    parser.addoption("--browser")



@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser=='Chrome':
        print("Launching Chrome Browser....!")
        driver=webdriver.Chrome()
    elif browser=='Firefox':
        print("Launching Firefox Browser....!")
        driver=webdriver.Firefox()
    elif browser=='IE':
        print("Launching IE Browser....!")
        driver=webdriver.Ie()
    elif browser=='Edge':
        print("Launching Edge Browser")
        driver=webdriver.Edge()
    else:
        opt=webdriver.ChromeOptions()
        opt.add_argument("--window-size=1920,1080")
        opt.add_argument("--start-maximized")
        opt.add_argument("--headless")
        # opt=webdriver.ChromeOptions()
        # opt.add_argument("headless")
        driver=webdriver.Chrome(options=opt)
    driver.maximize_window()
    return driver

