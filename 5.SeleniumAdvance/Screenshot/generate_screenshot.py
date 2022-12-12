from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class Screenshot():
    def capture_screenshot(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://google.com/')
        time.sleep(3)

        # Capture Screenshot
        driver.get_screenshot_as_file("E:\\BITM_Online_16\\Projects\\TestAutomationBITM16\\5.SeleniumAdvance"
                                      "\\Screenshot\\Screenshot_files\\GoogleScreenshot.png")

        driver.close()


test_obj = Screenshot()
test_obj.capture_screenshot()
