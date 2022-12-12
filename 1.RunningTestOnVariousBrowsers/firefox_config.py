from selenium import webdriver

def firefox_browser():
    # Browser launch
    driver = webdriver.Firefox(executable_path="E:\\BITM_Online_16\\Proejcts\\TestAutomationBITM16\\Drivers"
                                               "\\geckodriver.exe")

    # Open Website
    driver.get("https://www.google.com/")

    # Close Active Tab
    driver.close()

firefox_browser()