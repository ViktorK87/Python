from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
locator = ".btn.btn-primary"
driver.get("http://uitestingplayground.com/dynamicid")
button_dynamic_ID = driver.find_element(By.CSS_SELECTOR, locator)
button_dynamic_ID.click()
