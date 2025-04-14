from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/inputs")

input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
input.click()
input.send_keys("1000")
sleep(5)
input.clear()
sleep(5)
input.send_keys("999")
sleep(5)
driver.close()
