from elements import base
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


multiple_colors_ID="autoCompleteMultipleInput"
single_color_ID ="autoCompleteSingleInput"
multiple_color_xpath="//div[contains(@class,'auto-complete__menu-list')]//div"
single_color_xpath="//div[@class='auto-complete__menu-list css-11unzgr']//div"


"""This function will find auto complete tab and return driver"""
def auto_complete_web_element():
    driver=base.launch_browser()
    element=driver.find_element(By.XPATH,"//h5[text()='Elements']")
    base.execute_js_script(driver, element)
    auto_complete_element=driver.find_element(By.XPATH, "//span[text()='Auto Complete']")
    base.execute_js_script(driver, auto_complete_element)
    return driver
    
"""This function take color input from user to and return whether color found or not."""
def selecting_multiple_color_from_suggestions():
    colors=(input("Please enter colors you wants to select from suggestion with space : \n").split(" "))
    print("Color enter are : ")
    for color in colors:
        print(color)
    """ method will return True if found color else False"""
    driver=auto_complete_web_element()
    for color in colors:
        result=selecting_color_from_dropdown(driver,color,multiple_colors_ID,multiple_color_xpath)
        print(f"Color {color} Selected successfully." if (result)else f"Color {color} Not Found.")
    
    
            
""" take color and dropdown_xpath as input"""
def selecting_color_from_dropdown(driver,color,colors_ID,dropdown_xpath):
    driver.find_element(By.ID,colors_ID).send_keys(f"{color}")
    """ once enter color in textbox fetch all dropdown"""
    suggestions=WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.XPATH,dropdown_xpath)))
    actions=ActionChains(driver)
    for sugg_index, sugg in enumerate(suggestions,start=1):
        text=sugg.text.strip().lower()
        color_found=False
        """ as dropdown may be more so navigate through  ARROW_DOWN until found and then  ENTER"""
        if text in color:
            i=1
            while i<=sugg_index:
                actions.send_keys(Keys.ARROW_DOWN).perform()
                i +=1
                actions.send_keys(Keys.ENTER).perform()
                time.sleep(1)
                color_found=True
                break
    """ if found color retunr True else False"""
    if color_found:
        return True
    else:
        driver.find_element(By.ID,multiple_colors_ID).clear()
        return False

def select_single_color():
    color=input("PLease enter color do you want to select : \n")
    print(f"Color enter is : {color}")
    driver=auto_complete_web_element()
    driver=selecting_color_from_dropdown(driver,color,single_color_ID,single_color_xpath)
    
    
    
    
select_single_color()
selecting_multiple_color_from_suggestions()