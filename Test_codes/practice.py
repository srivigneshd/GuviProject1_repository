from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


class sriv:
    url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))


    def login(self):
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self.driver.title
    
    def login1(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(by=By.NAME,value='username').send_keys('Admin')
        self.driver.find_element(by=By.NAME,value='password').send_keys('admin123')
        self.driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        #xyw=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")       
        return self.driver.current_url
    
    def login2(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(by=By.NAME,value='username').send_keys('Admin')
        self.driver.find_element(by=By.NAME,value='password').send_keys('admin12345')
        self.driver.find_element(by=By.XPATH,value='/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        #xyw=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p")       
        return self.driver.title
    
print(sriv().login())
print(sriv().login1())
print(sriv().login2())
