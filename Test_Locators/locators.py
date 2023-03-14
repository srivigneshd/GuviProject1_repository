#MODULE FOR ORANGE HRM locators


class orange_locators:
    #LOCATORS REQURED FOR LOGIN TC1 AND TC2
    username_inputbox1='/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[1]/div[1]/div[2]/input[1]'        #XPATH
    username_inputbox='username'        #NAME
    password_inputbox='password'        #NAME
    submit_button='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'   #XPATH

    pim_button="/html[1]/body[1]/div[1]/div[1]/div[1]/aside[1]/nav[1]/div[2]/ul[1]/li[2]/a[1]/span[1]"       #XPATH
    pim_add_emp='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'  #XPATH
    
    #LOCATORS REQURED FOR PIM ADD EMPLOYEE AND EDIT EMPLOYEE 
    pim_personal_driv_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    pim_personal_dob_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'

    pim_personal_smoker_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span/i'
    pim_personal_gender_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    
    pim_personal_martial_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div'
    
    pim_personal_save_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'    #XPATH
    pim_personal_save2_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button' #XPATH  #XPATH

    pim_personal_military_loc='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'   
    pim_first_name_locator='firstName'        #NAME
    pim_middle_name_locator='middleName'      #NAME
    pim_last_name_locator='lastName'          #NAME
    pim_nickname_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    pim_emp_id_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input '   #xpath
    pim_emp_save_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'    #xpath

    #locators of personal_data
    pim_personal_driving_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    pim_personal_driving_exp_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    pim_personal_ssn_locators='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'
    pim_personal_sin_locators='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input'
    pim_personal_nationality_locator='/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    #pim_personal_nationality_locator="(//div[@class='oxd-select-text-input'][normalize-space()='India'])[1]"

    pim_edit_loc='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[22]/div/div[9]/div/button[2]'


    #testcase04 locators
    pim_personal_edit_loc="//div[@class='oxd-grid-4 orangehrm-full-width-grid']//div[1]//div[1]//div[2]//div[1]//div[1]//input[1]"
    pim_personal_empid_search_loc='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    pim_personal_empid_click_loc="(//i[@class='oxd-icon bi-check oxd-checkbox-input-icon'])[1]"
    pim_personal_emp_delclick_loc="//div[@role='columnheader']//i[@class='oxd-icon bi-check oxd-checkbox-input-icon']"
    pim_personal_emp_delclick2_loc="//button[normalize-space()='Delete Selected']"
    pim_personal_empall_loc="//div[@class='oxd-table-row oxd-table-row--with-border oxd-table-row--clickable']"