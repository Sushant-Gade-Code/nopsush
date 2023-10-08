import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class AddNewCustomer:
    link_CustomersMainmenu_XPATH = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]'
    link_CustomersSubmenuy_XPATH = '//ul[@class="nav nav-pills nav-sidebar flex-column nav-legacy"]/li[4]//ul/li[1]'
    Click_PIM_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("                          ")='PIM']")
    click_addNew_XPATH='//a[@class="btn btn-primary"]/i'
    input_Email_XPATH='//input[@id="Email"]'
    input_Password_XPATH ='//input[@id="Password"]'
    input_FirstName_XPATH ='//input[@id="FirstName"]'
    input_LastName_XPATH='//input[@id="LastName"]'
    radio_Male_XPATH='//div[@class="raw"]/div[1]/label'
    radio_Fmale_XPATH='//div[@class="raw"]/div[2]/label'
    input_DOB_XPATH='//input[@id="DateOfBirth"]'
    input_CompanyName_XPATH='//input[@id="Company"]'
    input_IsTaxExempt_XPATH='//input[@id="IsTaxExempt"]'
    input_NewsLatter_XPATH='//div[@class="card-body"]/div[9]/div[2]/div/div[1]/div'
    li_Your_Store_NAME_XPATH="//li[text()='Your store name']"
    li_Test_store_2_XPATH="//li[text()='Test store 2']"
    Select_NewsLatter_XPATH='//select[@id="SelectedNewsletterSubscriptionStoreIds"]'
    click_customer_roles='//div[@class="card-body"]/div[10]/div[2]/div/div[1]/div'
    li_Administrators_XPATH="//li[text()='Administrators']"
    li_Forum_Moderators_XPATH="//li[text()='Forum Moderators']"
    li_Guests_XPATH="//li[text()='Guests']"
    li_Registered_XPATH="//li[text()='Registered']"
    li_Vendors_XPATH="//li[text()='Vendors']"
    Select_Manage_of_vendor='//select[@id="VendorId"]'
    visible_text1='Vendor 1'
    visible_test2='Vendor 2'
    check_Active_XPATH="/input[@id='Active']"
    button_Save_XPATH='//button[@name="save"]'
    textarea_admin_content='//textarea[@id="AdminComment"]'


    def __init__(self,driver):
        self.driver=driver

    def getCustomermainmenu(self):
        self.aWait=WebDriverWait(self.driver,10,poll_frequency=2)
        self.aWait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.link_CustomersMainmenu_XPATH))).click()
        # self.driver.find_element(By.XPATH,self.Click_PIM_XPATH).click()

    def getCustomersubmenu(self):
        self.aWait.until(expected_conditions.element_to_be_clickable((By.XPATH, self.link_CustomersSubmenuy_XPATH))).click()
        self.driver.find_element(By.XPATH, self.link_CustomersSubmenuy_XPATH).click()

    def getAddnewButton(self):
        self.aWait.until(expected_conditions.element_to_be_clickable((By.XPATH,self.click_addNew_XPATH))).click()
        # self.driver.find_element(By.XPATH,self.click_addNew_XPATH).click()

    def getEmailid(self,emailid):
        # self.driver.find_element(By.XPATH,self.input_Email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_Email_XPATH).send_keys(emailid)

    def getPassword(self,password):
        self.driver.find_element(By.XPATH,self.input_Password_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_Password_XPATH).send_keys(password)

    def getFirstName(self,fname):
        self.driver.find_element(By.XPATH,self.input_FirstName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_FirstName_XPATH).send_keys(fname)

    def getLastName(self,fname):
        self.driver.find_element(By.XPATH,self.input_LastName_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_LastName_XPATH).send_keys(fname)

    def getRadioButton(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.radio_Male_XPATH).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.radio_Male_XPATH).click()
        else:
            self.driver.find_element(By.XPATH,self.radio_Male_XPATH).click()

    def getDOB(self,dob):
        self.driver.find_element(By.XPATH,self.input_DOB_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_DOB_XPATH).send_keys(dob)

    def getCompanyname(self,Companyname):
        self.driver.find_element(By.XPATH, self.input_CompanyName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_CompanyName_XPATH).send_keys(Companyname)

    def getIsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.input_IsTaxExempt_XPATH).click()

    def getNewsLatter(self,NewsLatter):
        self.driver.find_element(By.XPATH, self.input_NewsLatter_XPATH).click()
        if NewsLatter=="Your store name":
            self.driver.find_element(By.XPATH, self.li_Your_Store_NAME_XPATH).click()
        elif NewsLatter=="Test store 2":
            self.driver.find_element(By.XPATH, self.li_Test_store_2_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, self.li_Your_Store_NAME_XPATH).click()

    def getCustomerRoles(self, value):
        self.driver.find_element(By.XPATH, self.click_customer_roles).click()
        time.sleep(4)
        if value == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.li_Registered_XPATH)
        elif value == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.li_Administrators_XPATH)
        elif value == "Guests":
            time.sleep(4)
            self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
            time.sleep(2)
            self.listitem = self.driver.find_element(By.XPATH, self.li_Guests_XPATH)
        elif value == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.li_Registered_XPATH)
        elif value == "vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.li_Vendors_XPATH)
        elif value == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.li_Forum_Moderators_XPATH)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.listitem)


    # def getCustomerRoles(self,CustomerRoles):
    #     self.driver.find_element(By.XPATH,self.click_customer_roles).click()
    #     if CustomerRoles=='Administrators':
    #         self.driver.find_element(By.XPATH, self.li_Administrators_XPATH).click()
    #     elif CustomerRoles=='Forum Moderators':
    #         self.driver.find_element(By.XPATH, self.li_Forum_Moderators_XPATH).click()
    #     elif CustomerRoles=='Guests':
    #         time.sleep(5)
    #         self.driver.find_element(By.XPATH,'//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, self.li_Guests_XPATH).click()
    #     elif CustomerRoles == 'Registered':
    #         time.sleep(5)
    #         self.driver.find_element(By.XPATH, '//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]').click()
    #         time.sleep(2)
    #         self.driver.find_element(By.XPATH, self.li_Registered_XPATH).click()
    #     elif CustomerRoles == 'Vendors':
    #         self.driver.find_element(By.XPATH, self.li_Vendors_XPATH).click()
    #     else:
    #         self.driver.find_element(By.XPATH, self.li_Administrators_XPATH).click()

    def getmangerOfVender(self,mangerOfVender):
        e1=self.driver.find_element(By.XPATH,self.Select_Manage_of_vendor)
        dropele=Select(e1)
        if mangerOfVender=='Vendor 1':
            dropele.select_by_visible_text(self.visible_text1)
        elif mangerOfVender=='Vendor 2':
            dropele.select_by_visible_text(self.visible_test2)
        else:
            dropele.select_by_visible_text(self.visible_text1)

    def checkActive(self):
        self.driver.find_element(By.XPATH,self.check_Active_XPATH).click()

    def getAdminComment(self,admin_content):
        self.driver.find_element(By.XPATH,self.textarea_admin_content).clear()
        self.driver.find_element(By.XPATH,self.textarea_admin_content).send_keys(admin_content)

    def getSaveButton(self):
        self.driver.find_element(By.XPATH,self.button_Save_XPATH).click()








































