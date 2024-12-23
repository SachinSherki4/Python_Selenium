
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

chrome_driver=webdriver.Chrome()
chrome_driver.get(base_url)
actual_title=chrome_driver.title
print(f"Actual Ttitle of Home Page is : {actual_title}")
assert actual_title == "OrangeHRM" , "Title Mismatchh"
#time.sleep(3)
username=chrome_driver.find_element(By.NAME,"username")
username=WebDriverWait(chrome_driver,10).until(EC.visibility_of_element_located(username))
chrome_driver.username.send_keys("Admin")
password=chrome_driver.find_element(By.NAME,"password")
password=WebDriverWait(chrome_driver,10).until(EC.visibility_of_element_located(password))
chrome_driver.password.send_keys("admin123")
chrome_driver.find_element(By.XPATH, "//button[text()=' Login ']").click()
assert chrome_driver.title == "OrangeHRM", "Title Mismatch"

chrome_driver.close()
