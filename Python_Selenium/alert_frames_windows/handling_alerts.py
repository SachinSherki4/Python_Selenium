from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

base_url="https://testautomationpractice.blogspot.com/"
prompt_message="""Sachin Sherki"""

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(base_url)
simple_alert_popup=driver.find_element(By.ID, "alertBtn")
confirm_alert_popup=driver.find_element(By.ID, "confirmBtn")
prompt_alert_popup=driver.find_element(By.ID, "promptBtn")
window_popup=driver.find_element(By.ID, "PopUp")
alert_result=driver.find_element(By.ID,"demo")

def simple_alert():
    simple_alert_popup.click()
    alert= driver.switch_to.alert
    return alert

def confrmation_alert():
    confirm_alert_popup.click()
    alert=driver.switch_to.alert
    return alert

def prompt_alert():
    prompt_alert_popup.click()
    alert=driver.switch_to.alert
    return alert

accept_simple_alert=simple_alert()
accept_simple_alert.accept()
print("T_C_01 : To Accept Simple Alert Passed.")

accept_conf_alert=confrmation_alert()
accept_conf_alert.accept()
# assert alert_result.text =="You pressed OK!", "Accepting Alert Test Case Failed."
# print("Test Case to Accept Confirmation Alert Passed.")
# Below approch will not stop execution if test case failed.
print("T_C_02 : To Accept Confirmation Alert Passed." if (alert_result.text =="You pressed OK!") else AssertionError("T_C_02 : To Accept Confirmation Alert Failed."))

dismiss_conf_alert=confrmation_alert()
dismiss_conf_alert.dismiss()
# assert alert_result.text == "You pressed Cancel!", "Canceling Alert Test Case Failed."
# print("Test Case to Cancel Confirmation Alert Passed.")
print("T_C_03 : To Cancel Confirmation Alert Passed." if (alert_result.text == "You pressed Cancel!") else AssertionError("T_C_03 : To Cancel Confirmation Alert Failed."))

accept_promtAlert=prompt_alert()
accept_promtAlert.send_keys(prompt_message)
accept_promtAlert.accept()
print("T_C_04 : To Accept Prompt Alert Passed." if (alert_result.text == f"Hello {prompt_message}! How are you today?")else AssertionError("T_C_04 : To Accept Prompt Alert Failed."))

dismiss_promtAlert=prompt_alert()
dismiss_promtAlert.dismiss()
print("T_C_05 : To Cancel Prompt Alert Passed." if (alert_result.text == "User cancelled the prompt.") else AssertionError("T_C_05 : To Cancel Prompt Alert Failed."))

window_popup.click()
time.sleep(5)
window_handles=driver.window_handles
main_window=driver.current_window_handle
for window in window_handles:
    if window != main_window :
        driver.switch_to.window(window)
       # print("Window Title  : ",driver.title)
        driver.close()
        driver.switch_to.window(main_window)
       # print("Main window Title : ",driver.title)
print("T_C_06 : To switch on open window, close it and back to main window Passed." if (driver.title == "Automation Testing Practice") else AssertionError("T_C_06 : To switch on open window, close it and back to main window Failed."))    
    










