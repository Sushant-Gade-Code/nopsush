import random
import string
import time

from selenium.webdriver.common.by import By

from PageObjects.LoginPage import LoginPage
from PageObjects.add_new_customer import AddNewCustomer
from Utilities.Loggenerator import LogGenerator
from Utilities.Readproperties import Readconfig


class Test_add_new_customer_004:
    bseurl=Readconfig.getUrl()
    usernname=Readconfig.getuserEmail()
    password = Readconfig.getpassword()
    log=LogGenerator.loggen()

    def test_add_new_customer(self,setup):
        self.log.info('Test test_add_new_customer Started..!')
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
        # self.driver.maximize_window()
        time.sleep(2)
        self.lp2.getCustomermainmenu()
        self.log.info('Getting the getCustomermainmenu is Done....!')
        time.sleep(2)
        self.lp2.getCustomersubmenu()
        self.log.info('Getting the Customersubmenu is Done....!')
        time.sleep(8)
        self.lp2.getAddnewButton()
        self.log.info('Getting the getAddnewButton is Done....!')
        time.sleep(5)
        self.email = random_generator() + "@gmail.com"
        # self.log.info('Getting the random_generator function object creation is Done....!')
        time.sleep(2)
        self.lp2.getEmailid(self.email)
        self.log.info('Getting the random_generator Email is Done....!')
        time.sleep(2)
        self.lp2.getPassword('12345678')
        self.log.info('Getting the getPassword is Done....!')
        time.sleep(2)
        self.lp2.getFirstName('abc')
        self.log.info('Getting getFirstName is Done....!')
        time.sleep(2)
        self.lp2.getLastName('xyz')
        self.log.info('Getting getLastName is Done....!')
        time.sleep(2)
        self.lp2.getRadioButton('Male')
        self.log.info('Getting getRadioButton Male is Done....!')
        time.sleep(2)
        self.lp2.getDOB("10/05/1997")
        self.log.info('Getting getDOB  is Done....!')
        time.sleep(2)
        self.lp2.getCompanyname('Tata Ficosa')
        self.log.info('Getting getDOB  is Done....!')
        time.sleep(2)
        self.lp2.getIsTaxExempt()
        self.log.info('Getting getIsTaxExempt  is Done....!')
        time.sleep(2)
        self.lp2.getNewsLatter('Your store name')
        time.sleep(5)
        # self.lp2.getCustomerRoles("Administrators")
        # time.sleep(2)
        self.lp2.getCustomerRoles("Registered")
        self.log.info('Getting getCustomerRoles  is Done....!')
        time.sleep(2)
        self.lp2.getCustomerRoles("Vendors")
        self.log.info('Getting getCustomerRoles  is Done....!')
        time.sleep(2)
        self.lp2.getmangerOfVender('Vendor 2')
        self.log.info('Getting getmangerOfVender  is Done....!')
        time.sleep(2)
        # self.lp2.checkActive()
        time.sleep(2)
        self.lp2.getAdminComment('This is for practice')
        self.log.info('Getting getAdminComment  is Done....!')
        self.lp2.getSaveButton()
        self.log.info('Getting getSaveButton  is Done....!')
        time.sleep(2)
        self.msg=self.driver.find_element(By.TAG_NAME,'body').text
        self.log.info('Capturing body text  is Done....!')
        # exp_title='The new customer has been added successfully.'
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            self.log.info('Test test_add_new_customer Passed..!')
            assert True == True
            self.driver.save_screenshot('.\\Screenshots\\Test test_add_new_customer_Passed.png')
            self.lp.getLogOutButton()
            self.driver.close()
        else:
            self.driver.save_screenshot('.\\Screenshots\\Test test_add_new_customer_Failed.png')
            self.lp.getLogOutButton()
            self.driver.close()
            assert True == False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

