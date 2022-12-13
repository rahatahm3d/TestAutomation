from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time


class HeadlessTest():
    def headless_browser_chrome(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = False
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

        driver.get("https://google.com")
        time.sleep(3)

        def headless_browser_firefox(self):
            firefox_options = webdriver.FirefoxOptions()
            firefox_options.headless = True
            driver = webdriver.Firefox(GeckoDriverManager().install(), options=firefox_options)

            driver.get("https://apple.com")
            time.sleep(3)

            print(driver.title)

            driver.close()

        print(driver.title)

        driver.close()



test_obj = HeadlessTest()
test_obj.headless_browser_chrome()

