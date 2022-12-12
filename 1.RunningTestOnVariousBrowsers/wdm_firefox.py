from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def firefox_wdm():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get("https://google.com")

    driver.close()

firefox_wdm()