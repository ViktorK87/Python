from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox(service=FirefoxService(
    GeckoDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
input_username = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
input_password = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
login_button = driver.find_element(By.CSS_SELECTOR, '.fa.fa-2x.fa-sign-in')

input_username.send_keys("tomsmith")
input_password.send_keys("SuperSecretPassword!")
login_button.click()
sleep(5)
driver.close()
