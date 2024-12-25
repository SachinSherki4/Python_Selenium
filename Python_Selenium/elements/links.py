from selenium.webdriver.common.by import By
from elements import base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def link_element():
    driver=base.launch_browser()
    element=driver.find_element(By.XPATH, "//h5[text()='Elements']")
    base.execute_js_script(driver,element)
    ele=driver.find_element(By.XPATH, "//span[text()='Links']")
    base.execute_js_script(driver, ele)
    return driver
    
def compare_windos(handles,main_window):
    for handle in handles:
        if handle != main_window:
            return True
    return False
        
def home_link_opening_new_tab():
    driver=link_element()
    home_link=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"simpleLink")))
    home_link.click()
    main_window=driver.current_window_handle
    handles=driver.window_handles
    result=compare_windos(handles,main_window)
    if result:
        print("TC_01 : To click on Home Link to open new window is Passed." if (result)else AssertionError("TC_01 : To click on Home Link to open new window is Failed."))
    base.close_browser(driver)

def link_api_with_status_code():
    test_case_pass=True
    driver=link_element()
    link_element_present=["created","no-content","moved","bad-request","unauthorized","forbidden","invalid-url"]
    web_element_list=[]
    """ get attribute name from link_element_present and locate same element on webpage
         then add same element in one list web_element_list"""
    for element in link_element_present:
        try :
            ele=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,element)))
            web_element_list.append(ele)
        except Exception as e:
            test_case_pass=False
            print(f"Failed to locate element : '{element}' on web-page.: {e}")
    json_data=base.open_static_json_file()
    
    """ Now navigate each element - get its attribute and comapre it present in json 
        data and fetch related status and text and again verify that status annd text visible once we
          click on that web-element link"""
    for element in web_element_list:
        attribut=element.get_attribute("id")
        try :          
            if attribut in json_data:
                base.execute_js_script(driver, element)
                status=json_data[attribut]["status"]
                try :
                    status_display=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//b[text()='{status}']")))
                    text=json_data[attribut]["text"]
                    text_display=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,f"//b[text()='{text}']")))
                    assert status_display and text_display, "Test Case Failed."
                except Exception as e:
                    test_case_pass=False
                    print(f"Failed to locate '{attribut}' : status : {status_display} and text : {text_display}")
        except Exception as e :
            test_case_pass=False
            print(f"Attribute {attribut}not found in JSON data : {e}")
    if test_case_pass:
        print("TC_02 : To click all API and verify each status and Text Passed." if (test_case_pass)else AssertionError
              ("TC_02 : To click all API and verify each status and Text Failed."))
    base.close_browser(driver)

home_link_opening_new_tab()
link_api_with_status_code()


    
    