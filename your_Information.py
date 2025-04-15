from selenium.webdriver.common.by import By


class Your_information:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(3)

    def input_information(self, first_name, last_name, zip):
        self._driver.find_element(
            By.CSS_SELECTOR, "#first-name"
            ).send_keys(first_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "#last-name"
            ).send_keys(last_name)
        self._driver.find_element(
            By.CSS_SELECTOR, "#postal-code").send_keys(zip)
        self._driver.find_element(
            By.CSS_SELECTOR, "#continue").click()
