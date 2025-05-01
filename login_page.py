from selenium.webdriver.common.by import By
import allure

class Login_page:

    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.saucedemo.com/")
        self._driver.maximize_window()

    def login(self, user_name, password):
        """
            Авторизация в магазине
        """
        with allure.step("нахождение и подстановка имени"):
            self._driver.find_element(
                By.CSS_SELECTOR, "#user-name"
                    ).send_keys(user_name)
        with allure.step("нахождение и подстановка пароля"):
            self._driver.find_element(
                    By.CSS_SELECTOR, "#password"
                    ).send_keys(password)
        with allure.step("нажатие кнопки входа"):
            self._driver.find_element(
                    By.CSS_SELECTOR, "#login-button"
                    ).click()
