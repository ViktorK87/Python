from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class Calculator_use:
    def __init__(self, driver):
        """
            Эта функция инициализирует параметры класса
        """
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium" +
            "-webdriver-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay_input(self, delay: int):
        """
            Ф-я вводит в поле время задержки, предварительно удалив значение по дефолту
        """
        with allure.step("Нахождение поля ввода задержки и присвоение его в переменную"):
            input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        with allure.step("Очищение поля ввода"):
            input_delay.clear()
        with allure.step("Установка времени задержки"):
            input_delay.send_keys(str(delay))

    def input_number(self, number: int):
        """
            Ф-я вводит значение в калькулятор
        """
        with allure.step("Поиск кнопки с нужной цирой"):
            btn_nmbrs = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn-outline-primary"
            )
        with allure.step("Нажатие на нужную цифру"):
            for nmbr in btn_nmbrs:
                if nmbr.text == str(number):
                     nmbr.click()

    def operator(self, operator):
        """
            Ф-я вводит оператор  
        """
        with allure.step("Поиск кнопки оператора"):
            operators = self._driver.find_elements(
                By.CSS_SELECTOR, ".operator.btn.btn-outline-success"
                )
        with allure.step("Нажатие на нужный оператор"):
            for oper in operators:
                if oper.text == operator:
                    oper.click()

    def get_result(self) -> int:
        """
            Запускает вычисление и дожидается время ожидания вычисления и возвращает результат
        """
        with allure.step("Поиск и нажатие на ="):
            self._driver.find_element(
                By.CSS_SELECTOR, ".btn.btn-outline-warning"
                ).click()
        with allure.step("Поиск индикатора времени и ожидание нужного значения"):
            screen = self._driver.find_element(By.CSS_SELECTOR, ".screen")
            waiter = WebDriverWait(self._driver, 50)
            waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                        ".screen"), "15")
                        )
        with allure.step("Возврат результата"):
            return int(screen.text)
