from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


class Dropdown():
    def dropdown_select(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://the-internet.herokuapp.com/dropdown')
        time.sleep(5)

        dropdown_options = driver.find_element(By.CSS_SELECTOR, "select#dropdown")

        all_options = Select(dropdown_options)

        #all_options.select_by_value("1")

        #all_options.select_by_index(2)

        all_options.select_by_visible_text("Option 1")


test_obj = Dropdown()
test_obj.dropdown_select()
