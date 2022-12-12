from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


class MouseHover():
    def mouse_hover_action(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://demo.opencart.com/')
        time.sleep(3)

        mouse_action = ActionChains(driver)

        Desktop = driver.find_element(By.LINK_TEXT, "Desktops")
        mouse_action.move_to_element(Desktop).perform()
        time.sleep(2)

        Mac1 = driver.find_element(By.LINK_TEXT, "Mac (1)")
        Mac1.click()
        time.sleep(3)

        driver.close()


test_obj = MouseHover()
test_obj.mouse_hover_action()
