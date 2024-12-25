from selenium.webdriver.common.by import By
from elements import base
import time    

def text_box_element():
    driver=base.launch_browser()
    element=driver.find_element(By.XPATH, "//h5[text()='Elements']")
    base.execute_js_script(driver,element)
    text_box_ele=driver.find_element(By.XPATH,"//span[text()='Text Box']")
    base.execute_js_script(driver, text_box_ele)
    driver.find_element(By.ID,"userName").send_keys("Sachin")
    driver.find_element(By.ID,"userEmail").send_keys("abc@gmail.com")
    driver.find_element(By.ID,"currentAddress").send_keys("Akurdi Pune")
    driver.find_element(By.ID,"permanentAddress").send_keys("Akurdi Pune")
    time.sleep(5)
    driver.find_element(By.ID,"submit").click()
    print("TC_01 : Login Test Case Passed.")
    base.close_browser(driver)
    
text_box_element()
    
    
    
    
    
    
    
