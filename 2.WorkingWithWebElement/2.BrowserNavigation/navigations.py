from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Navigations():
    def browser_navigate(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get('https://www.google.com')

        driver.get('https://www.bbc.com')

        # Goes one step backward in the browser history.
        # back to google
        driver.back()

        # Goes one step forward in the browser history.
        # forward to BBC
        driver.forward()

        # Refreshes the current page.
        driver.refresh()

        driver.close()


test_obj = Navigations()
test_obj.browser_navigate()
