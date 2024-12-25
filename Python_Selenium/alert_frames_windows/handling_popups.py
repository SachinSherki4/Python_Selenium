from selenium import webdriver
from selenium.webdriver.common.by import By
import time

base_url="https://demoqa.com/"
window_page_url="https://demoqa.com/alertsWindows"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)

def execute_js_script(driver,element_exe):
    driver.execute_script("arguments[0].click()",element_exe)
    time.sleep(1)

def handliing_windows(driver):
    main_window=driver.current_window_handle
    window_handles=driver.window_handles
    for window in window_handles :
        if window != main_window :
            driver.switch_to.window(window)
            time.sleep(2)
            driver.close()
            driver.switch_to.window(main_window)
            time.sleep(4)
    

element=driver.find_element(By.XPATH, '//h5[contains(text(),"Alerts, Frame & Windows")]')
execute_js_script(driver, element)
driver.find_element(By.XPATH, "//span[contains(text(),'Browser Windows')]").click()
print(driver.title)
driver.find_element(By.ID,"tabButton").click()
handliing_windows(driver)
driver.find_element(By.ID,"windowButton").click()
handliing_windows(driver)
driver.find_element(By.ID,"messageWindowButton").click()
handliing_windows(driver)



