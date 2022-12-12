from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class BrowserInteract():
    def commands(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://www.google.com')

        # Returns the title of the current page.
        title = driver.title
        print(title)

        # Gets the URL of the current page.
        url = driver.current_url
        print(url)

        # print(driver.page_source)

        driver.close()


test_obj = BrowserInteract()
test_obj.commands()
