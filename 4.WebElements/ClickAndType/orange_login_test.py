from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


class Login_orange():
    def login_test_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)

        # Finding WebElements
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        # Type Email
        username.clear()
        username.send_keys("Admin")

        # Type Password
        password.clear()
        password.send_keys("admin123")

        # Click Login button
        login_button.click()

        time.sleep(3)

        driver.close()

    def login_test_invalid(self):
        def login_test_valid(self):
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

            driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
            time.sleep(5)

            # Finding WebElements
            username = driver.find_element(By.NAME, "username")
            password = driver.find_element(By.NAME, "password")
            login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

            # Type Email
            username.clear()
            username.send_keys("invalid username")

            # Type Password
            password.clear()
            password.send_keys("1234556")

            # Click Login button
            login_button.click()

            time.sleep(3)

            driver.close()


test_obj = Login_orange()
test_obj.login_test_valid()
test_obj.login_test_invalid()
