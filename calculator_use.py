from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calculator_use:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(
            "https://bonigarcia.dev/selenium" +
            "-webdriver-java/slow-calculator.html"
            )
        self._driver.implicitly_wait(4)
        self._driver.maximize_window()

    def delay_input(self, delay):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, "#delay")
        input_delay.clear()
        input_delay.send_keys(str(delay))

    def input_number(self, number):
        btn_nmbrs = self._driver.find_elements(
            By.CSS_SELECTOR, ".btn.btn-outline-primary"
            )
        for nmbr in btn_nmbrs:
            if nmbr.text == str(number):
                nmbr.click()

    def operator(self, operator):
        operators = self._driver.find_elements(
            By.CSS_SELECTOR, ".operator.btn.btn-outline-success"
            )
        for oper in operators:
            if oper.text == operator:
                oper.click()

    def get_result(self):
        self._driver.find_element(
            By.CSS_SELECTOR, ".btn.btn-outline-warning"
            ).click()
        screen = self._driver.find_element(By.CSS_SELECTOR, ".screen")
        waiter = WebDriverWait(self._driver, 50)
        waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,
                     ".screen"), "15")
                     )
        return int(screen.text)
