#pytest of Orange HRM using POM
#implicitly wait 

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager    # Webdriver manager for firefox browser
from selenium.webdriver.firefox.service import Service      
from selenium.webdriver.common.by import By
#from Test_Data.data import orange_data
#import Test_data.data as orange_data
#from Test_Locators.locators import orange_locators
import pytest
from Test_Data.data import orange_data

from Test_Locators.locators import orange_locators


class Test_OrangeHRM:
        #BOOTING METHOD FOR RUNNING THE PYTEST TEST CASES
    @pytest.fixture
    def boot(self):
        self.driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    
        # METHOD FOR LOGIN WITH VALID DATA

    def test_TC_Login_01(self,boot):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_inputbox).send_keys(orange_data().TC1_username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_inputbox).send_keys(orange_data().TC1_password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submit_button).click()
        assert self.driver.title=='OrangeHRM'
        print('TC1:The user is logged in successfully')

    #   # METHOD FOR LOGIN WITH IN-VALID DATA

    def test_TC_Login_02(self,boot):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_inputbox).send_keys(orange_data().TC2_username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_inputbox).send_keys(orange_data().TC2_password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submit_button).click()
        assert self.driver.title=='OrangeHRM'
        print('TC2:Invalid credentials not logged_in')

    def test_TC_pim_03(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_inputbox).send_keys(orange_data().TC1_username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_inputbox).send_keys(orange_data().TC1_password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submit_button).click()
        #pim program starts
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_button).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_add_emp).click()
        self.driver.find_element(by=By.NAME,value=orange_locators().pim_first_name_locator).send_keys(orange_data().pim_firstname)
        self.driver.find_element(by=By.NAME,value=orange_locators().pim_middle_name_locator).send_keys(orange_data().pim_middlename)
        self.driver.find_element(by=By.NAME,value=orange_locators().pim_last_name_locator).send_keys(orange_data().pim_lastname)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_emp_id_locator).send_keys(orange_data().pim_empid)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_emp_save_locator).click()
        #pim personal data
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_driving_locator).send_keys(orange_data().pim_personal_driving)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_driving_exp_locator).send_keys(orange_data().pim_personal_exp)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_ssn_locators).send_keys(orange_data().pim_personal_ssn)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_sin_locators).send_keys(orange_data().pim_personal_sin)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_nickname_locator).send_keys(orange_data().pim_nickname)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_driv_loc).send_keys(orange_data().pim_personal_driv)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_dob_loc).send_keys(orange_data().pim_personal_dob)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_smoker_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_gender_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_military_loc).send_keys(orange_data().pim_personal_military)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_save_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_save2_loc).click()
        # martial=self.driver.find_element(by=By.XPATH,value=self.pim_personal_martial_loc)
        # martial.click()
        # martial_dropdown=Select(martial)
        # martial_dropdown.select_by_visible_text('Single')

        # nationality=self.driver.find_element(by=By.XPATH,value=self.pim_personal_nationality_locator)
        # nationality.click()
        # nationality_dropdown=Select(nationality)
        # nationality_dropdown.select_by_visible_text('Indian')
        assert self.driver.title=="OrangeHRM"
        print("SUCCESSFULL EMPLOYEE ADDITION HAVE DONE....!")
       
         # METHOD FOR EMPLOYEE EDIT: TC_PIM 03
    def test_pim_edit_emp(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_inputbox).send_keys(orange_data().TC1_username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_inputbox).send_keys(orange_data().TC1_password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submit_button).click()
        #pim program starts
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_button).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_edit_loc).send_keys(orange_data().pim_personal_empname)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_empid_search_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_empid_click_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_empall_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_ssn_locators).send_keys(orange_data().pim_personal_ssn_reedit)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_save_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_save2_loc).click()
        assert self.driver.title=="OrangeHRM"
        print('Successful employee details addition....!')
        
    def test_pim_emp_del(self,boot):
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(orange_data().url)
        self.driver.find_element(by=By.NAME,value=orange_locators().username_inputbox).send_keys(orange_data().TC1_username)
        self.driver.find_element(by=By.NAME,value=orange_locators().password_inputbox).send_keys(orange_data().TC1_password)
        self.driver.find_element(by=By.XPATH,value=orange_locators().submit_button).click()
        #pim program starts
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_button).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_edit_loc).send_keys(orange_data().pim_personal_empname)
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_empid_search_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_emp_delclick_loc).click()
        self.driver.find_element(by=By.XPATH,value=orange_locators().pim_personal_emp_delclick2_loc).click()
        assert self.driver.title=="OrangeHRM"
        print('Done Successful Employee Deletion.!')
    

