from selenium import webdriver
import json
import os

base_url="https://demoqa.com/"
json_file_path=os.path.join(os.path.dirname(__file__),'..','test_data','status_text_static_data.json')

def launch_browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    return driver
    
def close_browser(driver):
    driver.close()

def execute_js_script(driver,element):
    driver.execute_script("arguments[0].click();",element)

def js_script_to_locate_element(driver,element):
    driver.execute_script("arguments[0].scrollIntoView();",element)
    
def open_static_json_file():
    with open(json_file_path,'r') as file :
        data=json.load(file)
        return data
