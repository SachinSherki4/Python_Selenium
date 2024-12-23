from selenium.webdriver.common.by import By
import time
from elements import launch_browser

driver=launch_browser.launching_browser()
element=driver.find_element(By.XPATH, "//h5[text()='Elements']")
driver.execute_script("arguments[0].click();",element)
time.sleep(4)
driver.find_element(By.XPATH,"//span[text()='Text Box']").click()
time.sleep(2)
driver.find_element(By.ID, "userName").send_keys("Automation Testing")
driver.find_element(By.ID,"userEmail").send_keys("automation@gmail.com")
driver.find_element(By.ID,"currentAddress").send_keys("Lets Learn Automation")
driver.find_element(By.ID,"permanentAddress").send_keys("Lets Learn Automation")
submit_button=driver.find_element(By.ID,"submit")
driver.execute_script("arguments[0].click();",submit_button)