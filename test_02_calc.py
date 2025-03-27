import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

input = driver.find_element(By.CSS_SELECTOR, ('#delay'))
input.send_keys('45')

btn_7 = driver.find_element(By.XPATH, ("//span[@class='btn btn-outline-primary' and text()='7']"))
btn_8 = driver.find_element(By.XPATH, ("//span[@class='btn btn-outline-primary' and text()='8']"))
btn_plus = driver.find_element(By.XPATH, ('//*[@id="calculator"]/div[2]/span[4]'))
btn_equals = driver.find_element(By.XPATH, ('//*[@id="calculator"]/div[2]/span[15]'))

btn_7.click()
btn_plus.click()
btn_8.click()
btn_equals.click()

waiter = WebDriverWait(driver, 45)
waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15"))

screen = driver.find_element(By.CSS_SELECTOR, ".screen")

def test_calculation():
    screen.text == 15

driver.close()