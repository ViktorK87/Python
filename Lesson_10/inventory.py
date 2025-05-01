from selenium.webdriver.common.by import By
import allure

class Inventory:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(3)

    def checkout(self):
        """
        переход на окно с заполнением данных
        """
        with allure.step("Нажатие кнопки checkout"):
            self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
