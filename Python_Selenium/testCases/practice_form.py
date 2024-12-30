from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
import time

base_url="https://demoqa.com/"
user_DOB ="25/10/1999"
image_path="C://Users/ssherki/Pictures/"
finding_sibling_xpath="/following-sibling::td"

data={
    "firstName" : "Sachin",
    "lastName" : "Sherki",
    "email" : "sa@gmail.com",
    "gender" : "Male",
    "mobile" : "6765656442",
    "address" : "1 Edgewater Drive",
    "state" : "Haryana",
    "city" : "Panipat",
    "picture" : "pic.jpg"
    }

def launch_browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    return driver

def execute_js_script(driver,element):
    driver.execute_script("arguments[0].click();",element)
    
def close_browser(driver):
    driver.close()
    
def practice_form_element():
    driver=launch_browser()
    element=driver.find_element(By.XPATH, "//h5[text()='Forms']")
    execute_js_script(driver,element)
    practice_form_ele=driver.find_element(By.XPATH,"//span[text()='Practice Form']")
    execute_js_script(driver, practice_form_ele)
    time.sleep(1)
    return driver

def filling_form_details():
    driver=practice_form_element()
    wait=WebDriverWait(driver,5)
    driver.find_element(By.ID, "firstName").send_keys(data["firstName"])
    driver.find_element(By.ID, "lastName").send_keys(data["lastName"])
    driver.find_element(By.ID,"userEmail").send_keys(data["email"])
    male_button=driver.find_element(By.ID,"gender-radio-1")
    execute_js_script(driver, male_button)
    driver.find_element(By.ID,"userNumber").send_keys(data["mobile"])
    driver.find_element(By.ID,"uploadPicture").send_keys(f"{image_path}{data['picture']}")
    driver.find_element(By.ID,"currentAddress").send_keys(data["address"])
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[text()='Select State']").click()
    actions=ActionChains(driver)
    state_options=driver.find_elements(By.XPATH,"//div[@class=' css-11unzgr']/div")
    state_found=False
    for state_index, state in enumerate(state_options,start=0):
        #print(state.text)
        if not (state.text== data["state"]):
            actions.send_keys(Keys.ARROW_DOWN)
        else :
            state_found=True
            state.click()
            
            break
    if not state_found:
        print("State Not Found.")
    time.sleep(1)
    city_dropdown=driver.find_element(By.XPATH,"//div[text()='Select City']")
    wait.until(EC.element_to_be_clickable((city_dropdown)))
    city_dropdown.click()
    avalable_city=driver.find_elements(By.XPATH,"//div[@class=' css-11unzgr']//div")
    city_select=False
    for city in avalable_city :
        if city.text == data["city"]:
            city.click()
            city_select=True
            break
    
    if city_select:
        pass
    else:
        print("City not Found.")
    time.sleep(1)
    
    driver.find_element(By.ID,"submit").click()
    time.sleep(1)
    verify_form_submited_data(driver,data)

def verify_form_submited_data(driver,data):
    Student_name=driver.find_element(By.XPATH,f"//td[text()='Student Name']{finding_sibling_xpath}").text
    student_email=driver.find_element(By.XPATH,f"//td[text()='Student Email']{finding_sibling_xpath}").text
    Gender=driver.find_element(By.XPATH,f"//td[text()='Gender']{finding_sibling_xpath}").text
    mobile=driver.find_element(By.XPATH,f"//td[text()='Mobile']{finding_sibling_xpath}").text
    Picture=driver.find_element(By.XPATH,f"//td[text()='Picture']{finding_sibling_xpath}").text
    Address=driver.find_element(By.XPATH,f"//td[text()='Address']{finding_sibling_xpath}").text
    State_City=driver.find_element(By.XPATH,f"//td[text()='State and City']{finding_sibling_xpath}").text
    
    Student_First_Last_Name=data["firstName"]+ " "+ data["lastName"]
    Student_State_City=data["state"]+" "+ data["city"]
    assert Student_First_Last_Name == Student_name, "Name Mismatch"
    assert data["email"] ==student_email, "Email Mismatch"
    assert data["gender"] == Gender, "Gender Mismatch"
    assert data["mobile"] == mobile, "Mobile Mismatch"
    assert data["picture"] == Picture ,"Picture Mismatch"
    assert data["address"] == Address, "Address Mismatch"
    assert Student_State_City == State_City, "State and City Mismatch"
    
    print("backend data verify successfully.")
    
    
filling_form_details()
