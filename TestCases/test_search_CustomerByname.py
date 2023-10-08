import random
import string
import time

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from PageObjects.Search_Customer import SearchCustomer
from PageObjects.add_new_customer import AddNewCustomer
from Utilities.Loggenerator import LogGenerator
from Utilities.Readproperties import Readconfig


class TestSearch_Customer_By_name_006:
    bseurl=Readconfig.getUrl()
    usernname=Readconfig.getuserEmail()
    password = Readconfig.getpassword()
    log=LogGenerator.loggen()

    def test_Search_Customer_By_name_006(self,setup):
        self.log.info('Test test_Search_Customer_005 Started..!')
        self.driver=setup
        self.log.info('Initalizing the insatnce of webdriver is Done..!')
        self.driver.implicitly_wait(10)
        self.driver.get(self.bseurl)
        self.log.info('Opening the URl is Done..!')
        self.lp=LoginPage(self.driver)
        self.log.info('Creating the Object of LoginPage class is Done..!')
        self.lp.getEmail(self.usernname)
        self.log.info('Getting the Email is Done..!')
        self.lp.getPassword(self.password)
        self.log.info('Getting the password is Done..!')
        self.lp.getLogInButton()
        self.log.info('Clicking the LogInButton is successfully ..!')
        time.sleep(5)
        self.lp2=AddNewCustomer(self.driver)
        self.log.info('Creating the Object of AddNewCustomer class is Done..!')
        time.sleep(2)
        self.lp2.getCustomermainmenu()
        self.log.info('Getting the getCustomermainmenu is Done....!')
        time.sleep(2)
        self.lp2.getCustomersubmenu()
        self.log.info('Getting the Customersubmenu is Done....!')
        time.sleep(2)
        self.lp3=SearchCustomer(self.driver)
        time.sleep(2)
        self.lp3.getFirstName("Virat")
        time.sleep(2)
        self.lp3.getLastName('Kohli')
        time.sleep(2)
        self.lp3.getSearchButton()
        time.sleep(2)
        time.sleep(5)
        status = self.lp3.searchCustomerByName("Virat Kohli")
        assert True == status
        self.driver.close()

