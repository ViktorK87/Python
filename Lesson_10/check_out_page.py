from selenium.webdriver.common.by import By
import allure


class Check_out_page():
    def __init__(self, driver):
        self._driver = driver

    def get_total_summ(self) -> int:
        """
            Получение итоговой стоимости покупок
        """
        with allure.step("Нахождение итоговой суммы"):
            price = self._driver.find_element(
                By.CSS_SELECTOR, '.summary_total_label'
                ).text    
            n = 0
            new_price = price[:n] + price[n+7:]
            return new_price
