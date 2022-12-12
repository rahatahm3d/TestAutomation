from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class Locator():
    def locator_findings(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)

        username = driver.find_element(By.NAME, "username")

        if username is not None:
            print('username found Successfully by Name')
        else:
            print('username not found !!')

        driver.close()


test_obj = Locator()
test_obj.locator_findings()