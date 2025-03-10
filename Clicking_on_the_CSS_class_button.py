from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

button_locator = ".btn.btn-primary"

button = driver.find_element(By.CSS_SELECTOR, button_locator)

button.click()
