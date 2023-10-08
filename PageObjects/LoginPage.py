from selenium.webdriver.common.by import By


class LoginPage:
    input_Email_XPATH='//input[@id="Email"]'
    input_Password_XPATH='//input[@id="Password"]'
    click_Loginbutton_XPATH='//button[text()="Log in"]'
    click_LogOutbutton_XPATH="//a[text()='Logout']"


    def __init__(self,driver):
        self.driver=driver

    def getEmail(self,email):
        self.driver.find_element(By.XPATH,self.input_Email_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_Email_XPATH).send_keys(email)

    def getPassword(self,password):
        self.driver.find_element(By.XPATH,self.input_Password_XPATH).clear()
        self.driver.find_element(By.XPATH,self.input_Password_XPATH).send_keys(password)

    def getLogInButton(self):
        self.driver.find_element(By.XPATH,self.click_Loginbutton_XPATH).click()

    def getLogOutButton(self):
        self.driver.find_element(By.XPATH,self.click_LogOutbutton_XPATH).click()




