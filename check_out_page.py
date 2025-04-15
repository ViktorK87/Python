from selenium.webdriver.common.by import By


class Check_out_page():
    def __init__(self, driver):
        self._driver = driver

    def get_total_summ(self):
        price = self._driver.find_element(
            By.CSS_SELECTOR, '.summary_total_label'
            ).text
        n = 0
        new_price = price[:n] + price[n+7:]
        return new_price
