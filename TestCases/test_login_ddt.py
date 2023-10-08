
#  pytest -rA --html=.\\Reports\\report1.html --browser=Chrome

import time
from Utilities.Loggenerator import LogGenerator
from Utilities.Readproperties import Readconfig
from Utilities.Xlutilities import Xlutility
from PageObjects.LoginPage import LoginPage
class Test_login_ddt_002:
    baseurl=Readconfig.getUrl()
    file="C:\\Users\\Admin\\PycharmProjects\\nopsush.py\\TestData\\testData.xlsx"
    rows=Xlutility.getRowsCount(file,'Sheet1')
    log=LogGenerator.loggen()

    def test_login_ddt(self,setup):
        self.log.info('Test test_login_ddt Started..!')
        self.driver=setup
        self.log.info('Initializing driver is done..!')
        self.driver.get(self.baseurl)
        self.log.info('Opening Url Is successfully..!')
        self.lp=LoginPage(self.driver)
        self.log.info('Creating object of an LoginPage class is sucesfully..!')
        aList = []
        for r in range(2, self.rows+1):
            useremail=Xlutility.getReadData(self.file,'Sheet1',r,1)
            self.log.info('Getting useremail  is sucesfully..!')
            userpass=Xlutility.getReadData(self.file,'Sheet1',r,2)
            self.log.info('Getting userpass  is sucesfully..!')
            status=Xlutility.getReadData(self.file,'Sheet1',r,3)
            self.log.info('Getting status  is sucesfully..!')
            self.lp.getEmail(useremail)
            self.log.info('Paasing useremail into email field  is sucesfully..!')
            self.lp.getPassword(userpass)
            self.log.info('Paasing userpass into Password field  is sucesfully..!')
            time.sleep(2)
            self.lp.getLogInButton()
            self.log.info('Getting LogInButton is sucesfully..!')
            act_title=self.driver.title
            self.log.info('Capturing act_title is sucesfully..!')
            exp_title='Dashboard / nopCommerce administration'
            if act_title==exp_title:
                self.log.info('Test test_login_ddt Passed..!')
                if status=='Pass':
                    self.log.info('Test status is Pass..!')
                    aList.append('Pass')
                    self.log.info('Pass is add into emptyList..!')
                    self.lp.getLogOutButton()
                    self.log.info('Getting LogOutButton is Successfully..!')
                    time.sleep(5)
                elif status=='Fail':
                    self.log.info('Test status is Fail..!')
                    aList.append('Fail')
                    self.log.info('Fail is add into emptyList..!')
                    self.lp.getLogOutButton()
                    self.log.info('Getting LogOutButton is Successfully..!')
                    time.sleep(5)
            elif  act_title!=exp_title:
                self.log.info('Test test_login_ddt Failed..!')
                if status=='Fail':
                    self.log.info('Test status is Fail..!')
                    aList.append('Pass')
                    self.log.info('Fail is add into emptyList..!')
                    time.sleep(5)
                elif status=='Pass':
                    self.log.info('Test status is Fail..!')
                    aList.append('Fail')
                    self.log.info('Fail is add into emptyList..!')
                    time.sleep(5)
        self.driver.close()
        self.log.info('Closing active window is done..!')
        print(aList)

        if 'Fail' not in aList:
                self.log.info('Tata driven testing is pass..!')
                # self.driver.save_screenshot(".\\Screenshots\\Tata_driven_testing_is_Pass.png")
                assert True

        else:
                self.log.info('Tata driven testing is Failed..!')
                # self.driver.save_screenshot(".\\Screenshots\\Tata_driven_testing_is_Faled.png")
                assert False













