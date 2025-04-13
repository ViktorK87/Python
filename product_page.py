from selenium.webdriver.common.by import By


class Product_page:
    def __init__(self, driver):
        self._driver = driver
        self._driver.implicitly_wait(3)

    def add_product(self):
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie'
            ).click()
        self._driver.find_element(
            By.CSS_SELECTOR, '.shopping_cart_link').click()
