from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from widgets import date_formatting
import time

user_enter_date="29 December 2024"
base_url="https://seleniumpractise.blogspot.com/search?q=date"
date_picker="datepicker"
year_class="ui-datepicker-year"
month_class="ui-datepicker-month"
calender_class="ui-datepicker-calendar"
calender_next_button_xpath="//span[text()='Next']"
calender_prev_button="//span[text()='Prev']"

""" 
1. first compare user_date format => "parse_date_to_know_format(date)"
2. convert it into required format => "convert_date_to_new_format(date, date_format, "%Y %B %d")"
3. Capture current date and convert it to require format.
4. Compare user date is previous or future
5. Accordingly select date from Calender. """

def launch_browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    return driver
    


def select_date_from_calender(user_date):
    driver=launch_browser()
    driver.find_element(By.ID,date_picker).click()
    """update user date format and verify is it future date or previous date"""
    is_future_date, updated_user_date=date_formatting.format_user_date(user_date)
    year,month,date=updated_user_date.split(" ")
    WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.CLASS_NAME,calender_class)))
    current_month=driver.find_element(By.CLASS_NAME,month_class).text
    current_year=driver.find_element(By.CLASS_NAME,year_class).text
    
    """ set navigation button based on future or current date"""
    calender_navigation_button=""
    if is_future_date :
        calender_navigation_button=calender_next_button_xpath
    else :
        calender_navigation_button=calender_prev_button
    
    """If date is future of previous navigate until year and month appears using while loop"""
    while not(current_month.__eq__(month) and current_year.__eq__(year)):
        driver.find_element(By.XPATH,calender_navigation_button).click()
        current_month=driver.find_element(By.CLASS_NAME,month_class).text
        current_year=driver.find_element(By.CLASS_NAME,year_class).text
    date_xpath=f"//td[@data-handler='selectDay']/a[text()='{date}']"
    driver.find_element(By.XPATH,date_xpath).click()
    time.sleep(5)
    driver.quit()

"""change user_enter_date accordingly and call this method to select that date """
select_date_from_calender(user_enter_date)

    
    
    
    