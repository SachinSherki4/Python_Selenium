from selenium.webdriver.common.by import By
from elements import launch_browser
import time

driver=launch_browser.launching_browser()
check_box=driver.find_element(By.XPATH, "//span[text()='Check Box']")
driver.execute_script("arguments[0].click();",check_box)
driver.find_element(By.CLASS_NAME,"rct-icon rct-icon-expand-close").click()

