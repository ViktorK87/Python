from selenium.webdriver.common.by import By
import allure

class Your_information:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(3)

    def input_information(self, first_name: str, last_name: str, zip: int):
        """
            подстановка личных данных
        """
        with allure.step("вставка в поле ввода имя"):
            self._driver.find_element(
                By.CSS_SELECTOR, "#first-name"
                ).send_keys(first_name)
        with allure.step("ввод в поле фамилию"):
            self._driver.find_element(
                By.CSS_SELECTOR, "#last-name"
                ).send_keys(last_name)
        with allure.step("вставка в поле зип код"):
            self._driver.find_element(
                By.CSS_SELECTOR, "#postal-code").send_keys(zip)
        with allure.step("нажатие кнопки продолжить"):
            self._driver.find_element(
                By.CSS_SELECTOR, "#continue").click()
