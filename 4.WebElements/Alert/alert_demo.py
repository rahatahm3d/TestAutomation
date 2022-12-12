from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class Alert():
    def handle_alert(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://the-internet.herokuapp.com/javascript_alerts')
        time.sleep(3)

        # Normal Alert
        normal_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > button")
        normal_alert.click()

        driver.switch_to.alert.accept()  # Click on OK
        time.sleep(3)

        # Confirm Alert
        confirm_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(2) > button")
        confirm_alert.click()

        driver.switch_to.alert.dismiss()  # Click on Cancel
        time.sleep(2)

        # Prompt Alert
        prompt_alert = driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(3) > button")
        prompt_alert.click()

        # driver.switch_to.alert.send_keys("TestAutomationBITM16")
        driver.switch_to.alert.dismiss()
        time.sleep(2)

        driver.close()


test_obj = Alert()
test_obj.handle_alert()
