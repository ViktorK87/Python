from selenium.webdriver.common.by import By


class Inventory:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(3)

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
