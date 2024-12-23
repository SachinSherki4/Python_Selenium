from selenium import webdriver
from selenium.webdriver.common.by import By
import  time

base_url="https://demoqa.com/"
window_page_url="https://demoqa.com/alertsWindows"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)


element=driver.find_element(By.XPATH, '//h5[contains(text(),"Alerts, Frame & Windows")]')
driver.execute_script("arguments[0].click();",element)
time.sleep(2)
frame=driver.find_element(By.XPATH,"//span[text()='Frames']")
driver.execute_script("arguments[0].click();",frame)
time.sleep(4)
iframe_id=driver.find_element(By.ID,"frame1")
driver.switch_to.frame("frame1")

print(driver.title)
print(driver.current_url)
