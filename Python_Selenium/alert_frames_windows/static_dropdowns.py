from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import  Select


base_url= "https://testautomationpractice.blogspot.com/"
home_title="Automation Testing Practice"
driver=webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
assert driver.title==home_title, "Test Case Failed, as Title of page is not match."
country_element=driver.find_element(By.ID,"country")
color_element=driver.find_element(By.ID, "colors")
country=Select(country_element)
options=country.options
country_found=False
print("Dropdown Single Select :")
for option in options:
    if option.text == "Canada":
        option.click()
        country_found=True
        break
if country_found:
    print("We have successffully found expected country in list.")
else:
    print("Not found expected Country in country list.")
    
print("Dropdown Multi-Select : ")
colors=Select(color_element)
color_options=colors.options
for option in color_options:
    if option.text == "Red" or option.text == "White" or option.text == "Green" : 
        option.click()
    else:
        continue
time.sleep(2)

color_selected=colors.all_selected_options
print("Colors selected from dropdown list are : ")
for item in color_selected:
    print(item.text)
    
print("Dynamic Dropdown select")

print("Handling Date dropdown : ")