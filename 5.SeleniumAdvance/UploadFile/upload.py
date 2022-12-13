from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

class FileUpload():
    def upload_file(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://the-internet.herokuapp.com/upload')
        time.sleep(3)

        choose_file_btn = driver.find_element(By.ID, "file-upload")
        choose_file_btn.send_keys("D:\\SQA_Class\\Tools\\rht.jpg")

        upload_btn = driver.find_element(By.ID, "file-submit")
        upload_btn.click()
        time.sleep(2)

        driver.close()


test_obj = FileUpload()
test_obj.upload_file()