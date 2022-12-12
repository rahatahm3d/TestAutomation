from selenium import webdriver

def chrome_browser():
    # Browser launch
    driver = webdriver.Chrome(executable_path="E:\\BITM_Online_16\\Proejcts\\TestAutomationBITM16\\Drivers"
                                               "\\chromedriver.exe")

    # Open Website
    driver.get("https://www.google.com/")

chrome_browser()