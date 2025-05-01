from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from login_page import Login_page
from product_page import Product_page
from your_Information import Your_information
from inventory import Inventory
from check_out_page import Check_out_page
import allure

@allure.severity("blocker")


@allure.title("Проверка итоговой стоимости покупок")
@allure.description("Вход, добавление в корзину, заполнение данных, покупка и проверка итоговой стоимости")
def test_final_price():
    """
        покупка товаров и проверка итоговой стоимости
    """
    driver = webdriver.Chrome(
    service = ChromeService(ChromeDriverManager().install()))
    login_page = Login_page(driver)
    product_page = Product_page(driver)
    your_information = Your_information(driver)
    inventory = Inventory(driver)
    check_out_page = Check_out_page(driver)

    login_page.login("standard_user", "secret_sauce")
    product_page.add_product()
    inventory.checkout()
    your_information.input_information("Viktor", "family", "123456")
    
    final_price = check_out_page.get_total_summ()
    assert final_price == "$58.29"
    driver.quit()

