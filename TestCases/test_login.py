from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from Utilities.Loggenerator import LogGenerator
from Utilities.Readproperties import Readconfig

class Test_login:
    baseUrl=Readconfig.getUrl()
    emial=Readconfig.getuserEmail()
    password=Readconfig.getpassword()
    log=LogGenerator.loggen()

    def test_HomePage_title_01(self,setup):
        self.log.info('Test test_HomePage_title__001 Started..!')
        self.driver=setup
        self.log.info('Initialization driver Is Done..!')
        self.driver.get(self.baseUrl)
        self.log.info('Opening The Url is Succssfully..!')
        act_title=self.driver.title
        self.log.info('Capturing act_title is Done ..!')
        exp_title="Your store. Login"
        if act_title==exp_title:
            self.log.info('Test test_HomePage_title__001 Passed..!')
            assert True
            self.driver.save_screenshot(".\\Screenshots\\test_HomePage_title_Passed.png")
            self.log.info('Capturing Screenshots of test_HomePage_title_Passed.png is Done ..!')
            self.driver.close()
            self.log.info('Closing active window  is Done ..!')
        else:
            self.log.info('Test test_HomePage_title__001 Failed..!')
            self.driver.save_screenshot(".\\Screenshots\\test_HomePage_title_Failed.png")
            self.log.info('Capturing Screenshots of test_HomePage_title_Failed.png is Done ..!')
            self.driver.close()
            self.log.info('Closing active window  is Done ..!')
            assert False


    def test_LoginPage_title_02(self,setup):
        self.log.info('Test test_LoginPage_title_02 Started..!')
        self.driver=setup
        self.log.info('Initializing the driver is Done..!')
        self.driver.get(self.baseUrl)
        self.log.info('Opening The Url is Succssfully..!')
        self.lp=LoginPage(self.driver)
        self.log.info('Creating of an object Of LoginPage class is done ..!')
        self.lp.getEmail(self.emial)
        self.log.info('Getting useremail is done ..!')
        self.lp.getPassword(self.password)
        self.log.info('Getting userpassword is done ..!')
        self.lp.getLogInButton()
        self.log.info('Getting LogInButton is Succesfully ..!')
        act_title=self.driver.title
        self.log.info('Capturing act_title is Done ..!')
        exp_title='Dashboard / nopCommerce administration'
        if act_title==exp_title:
            self.log.info('Test test_LoginPage_title_02 Passed..!')
            assert True
            self.driver.save_screenshot('.\\Screenshots\\test_LoginPage_title_passed.png')
            self.log.info('Capturing Screenshot of test_LoginPage_title_passed.png..!')
            self.lp.getLogOutButton()
            self.log.info('Getting LogOutButton is Succesfully ..!')
        else:
            self.log.info('Test test_LoginPage_title_02 Failed..!')
            self.driver.save_screenshot('.\\Screenshots\\test_LoginPage_title_Failed.png')
            self.log.info('Capturing Screenshot of test_LoginPage_title_Failed.png..!')
            self.driver.close()
            self.log.info('Closing active window  is Done ..!')
            assert False
















