from selenium.webdriver.common.by import By
from elements import base
import time

driver=base.launch_browser()
check_box=driver.find_element(By.XPATH, "//span[text()='Check Box']")
driver.execute_script("arguments[0].click();",check_box)
driver.find_element(By.CLASS_NAME,"rct-icon rct-icon-expand-close").click()

