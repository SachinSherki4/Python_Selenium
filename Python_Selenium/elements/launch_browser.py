from selenium import webdriver

base_url="https://demoqa.com/"
def launching_browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)
    return driver
