from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, ".form-control")
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")

input.click()
input.send_keys("SkyPro")
button.click()
print(button.text)

driver.quit()
