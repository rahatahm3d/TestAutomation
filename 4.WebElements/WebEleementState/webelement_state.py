from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class State():
    def check_state(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)

        # Finding WebElements
        username = driver.find_element(By.NAME, "username")

        username_display_state = username.is_displayed()
        username_enable_state = username.is_enabled()  # True if username is enabled or False otherwise

        if username_display_state and username_enable_state == True:
            username.send_keys("Admin")
        else:
            print("Username field is inactive or display hide.This is Bug")

        # Checking password field
        password = driver.find_element(By.NAME, "password")

        password_display_state = password.is_displayed()
        password_enable_state = username.is_enabled()  # True if username is enabled or False otherwise

        if password_display_state and password_enable_state == True:
            password.send_keys("Admin")
        else:
            print("password field is inactive or display hide.This is Bug")

        time.sleep(3)

        driver.close()


test_obj = State()
test_obj.check_state()
