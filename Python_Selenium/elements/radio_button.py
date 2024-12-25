from selenium.webdriver.common.by import By
from elements import base
import time
    
def radio_button_element():
    driver=base.launch_browser()
    element=driver.find_element(By.XPATH, "//h5[text()='Elements']")
    base.execute_js_script(driver,element)
    radio_button_ele=driver.find_element(By.XPATH,"//span[text()='Radio Button']")
    base.execute_js_script(driver, radio_button_ele)
    time.sleep(5)
    return driver

def click_yes_radio_button():
    driver=radio_button_element()
    yes_button=driver.find_element(By.ID,"yesRadio")
    base.execute_js_script(driver, yes_button)
    yes_message=driver.find_element(By.XPATH,"//span[text()='Yes']").text
    print("TC_01 : To click on Yes Radio Button is Passed." if (yes_message == "Yes")else AssertionError("TC_01 : To click on Yes Radio Button is Failed."))
    base.close_browser(driver)

def click_Immpresive_radio_button():
    driver=radio_button_element()
    impressive_button=driver.find_element(By.ID,"impressiveRadio")
    base.execute_js_script(driver, impressive_button)
    impressive_message=driver.find_element(By.XPATH,"//span[text()='Impressive']").text
    print("TC_02 : To Impressive on Yes Radio Button is Passed." if (impressive_message == "Impressive")else AssertionError("TC_02 : To click on Impressive Radio Button is Failed."))
    base.close_browser(driver)

click_yes_radio_button()
click_Immpresive_radio_button()





