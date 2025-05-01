from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_use import Calculator_use
import allure


@allure.severity("blocker")
@allure.title("Сложение двух чисел")
@allure.feature("Вычисление")
@allure.description("Сложение двух чисел с получением результата")
def test_calculator():
    with allure.step("Подключение драйвера гугл хром"):
        driver = webdriver.Chrome(
                    service=ChromeService(ChromeDriverManager().install())
                    )
    with allure.step("Передача драйвера в класс калькулятора"):
        calculator_use = Calculator_use(driver)
    with allure.step("Ввод времени задержки"):    
        calculator_use.delay_input(45)
    with allure.step("Ввод первого числа"):
        calculator_use.input_number(7)
    with allure.step("Ввод операнда"):
        calculator_use.operator("+")
    with allure.step("Ввод второго числа"):
        calculator_use.input_number(8)
    with allure.step("Сравнение разультата с нужным значением"):
        assert calculator_use.get_result() == 15
    with allure.step("Закрытие драйвера"):
        driver.quit()
