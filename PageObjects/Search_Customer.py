from selenium.webdriver.common.by import By


class SearchCustomer:
    input_Email_XPATH='//input[@id="SearchEmail"]'
    input_FirstName_XPATH='//input[@id="SearchFirstName"]'
    input_LastName_XPATH='//input[@id="SearchLastName"]'
    click_Search_XPATH='//button[@id="search-customers"]'
    table_XPATH='//table[@id="customers-grid"]'
    table_Rows='//table[@id="customers-grid"]/tbody/tr'
    table_Column='//table[@id="customers-grid"]/thead/tr/th'

    def __init__(self,driver):
        self.driver=driver

    def getEmail(self,searchEmail):
        self.driver.find_element(By.XPATH,self.input_Email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_Email_XPATH).send_keys(searchEmail)

    def getFirstName(self, SearchFirstName):
        self.driver.find_element(By.XPATH, self.input_FirstName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_FirstName_XPATH).send_keys(SearchFirstName)

    def getLastName(self, SearchLastName):
        self.driver.find_element(By.XPATH, self.input_LastName_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_LastName_XPATH).send_keys(SearchLastName)

    def getSearchButton(self):
        self.driver.find_element(By.XPATH, self.click_Search_XPATH).click()


    def getNumberOfRows(self):
        return(len(self.driver.find_elements(By.XPATH,self.table_Rows)))


    def searchCustomerByEmail(self,email):
        flag = False
        for r in range(1,self.getNumberOfRows()+1):
            table=self.driver.find_element(By.XPATH,self.table_XPATH)
            emailid = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[2]').text
            if emailid==email:
                flag=True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNumberOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_XPATH)
            name = table.find_element(By.XPATH, '//*[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]').text
            if name == Name:
                flag = True
                break
        return flag

