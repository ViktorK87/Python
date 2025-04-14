from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from calculator_use import Calculator_use


def test_calculator():
    driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
                )
    calculator_use = Calculator_use(driver)
    calculator_use.delay_input(45)
    calculator_use.input_number(7)
    calculator_use.operator("+")
    calculator_use.input_number(8)
    assert calculator_use.get_result() == 15

    driver.quit()
