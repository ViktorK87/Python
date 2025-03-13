from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )
driver.fullscreen_window()
waiter = WebDriverWait(driver, 40)
waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#text"), "Done!")
)

image = driver.find_element(By.CSS_SELECTOR, "#award")
atribute_src = image.get_property("src")
print("Атрибут = ", atribute_src)
driver.quit()
