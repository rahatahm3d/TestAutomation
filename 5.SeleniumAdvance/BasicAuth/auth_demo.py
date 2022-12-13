from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


class BasicAuthentication():
    def auth_handle(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        # Formula: protocol://username:password@host:port
        driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

        time.sleep(5)

        print(driver.title)

        driver.close()


test_obj = BasicAuthentication()
test_obj.auth_handle()
