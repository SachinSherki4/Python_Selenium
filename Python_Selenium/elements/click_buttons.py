from selenium.webdriver.common.by import By
from elements import base
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

single_click_message="You have done a dynamic click"
right_click_message="You have done a right click"
double_click_message="You have done a double click"


def check_button_element():
    driver=base.launch_browser()
    element=driver.find_element(By.XPATH, "//h5[text()='Elements']")
    base.execute_js_script(driver,element)
    button=driver.find_element(By.XPATH, "//span[text()='Buttons']")
    base.execute_js_script(driver, button)
    return driver
    
def perform_action(driver):
        actions=ActionChains(driver)
        return actions

def single_click_functionality():
    driver=check_button_element()
    ele=driver.find_element(By.XPATH, "//button[text()='Click Me']")
    actions=perform_action(driver)
    actions.click(ele).perform()
    single_click=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='You have done a dynamic click']"))).text
    #single_click=driver.find_element(By.XPATH,"//p[text()='You have done a dynamic click']").text
    print("TC_01 : To Single click on button Passed." if (single_click == single_click_message) else AssertionError("TC_01 : To Single click on button Failed."))
    base.close_browser(driver)
    
def double_click_functionality():
    driver=check_button_element()
    ele=driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
    actions=perform_action(driver)
    actions.double_click(ele).perform()
    double_click=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='You have done a double click']"))).text
    #double_click_mess=driver.find_element(By.XPATH,"//p[text()='You have done a double click']")
    print("TC_02 : To Double click on button Passed." if (double_click == double_click_message) else AssertionError("TC_02 : To Double click on button Failed."))
    base.close_browser(driver)
    
def right_click_functionality():
    driver=check_button_element()
    ele=driver.find_element(By.XPATH, "//button[text()='Right Click Me']")
    actions=perform_action(driver)
    actions.context_click(ele).perform()
    right_click=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//p[text()='You have done a right click']"))).text
    #right_click=driver.find_element(By.XPATH, "//p[text()='You have done a right click']")
    print("TC_03 : To Right click on button Passed." if (right_click == right_click_message) else AssertionError("TC_03 : To Right click on button Failed."))
    base.close_browser(driver)
    
    
single_click_functionality()
double_click_functionality()
right_click_functionality()
