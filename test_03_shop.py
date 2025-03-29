import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")

input_user = driver.find_element(By.CSS_SELECTOR,
                                 (".input_error[placeholder='Username']")
                                 )
input_pswrd = driver.find_element(By.CSS_SELECTOR,
                                  (".input_error[placeholder='Password']")
                                  )
btn_login = driver.find_element(By.CSS_SELECTOR, ('.submit-button'))

input_user.send_keys("standard_user")
input_pswrd.send_keys("secret_sauce")
btn_login.click()

driver.find_element(By.CSS_SELECTOR,
                    "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR,
                    "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Viktor")
driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Kanunnikov")
driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("111401")
driver.find_element(By.CSS_SELECTOR, "#continue").click()
total = driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
driver.close()

last_total = "$" + re.findall(r'\d+', total)[0] + \
             "." + re.findall(r'\d+', total)[1]


def test_total_summ():
    assert last_total == "$58.29"


driver.close()
