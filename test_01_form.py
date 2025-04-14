from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )
driver.fullscreen_window()

input_first_name = driver.find_element(By.CSS_SELECTOR,
                                       ('.form-control[name=first-name]')
                                       )
input_last_name = driver.find_element(By.CSS_SELECTOR,
                                      (".form-control[name=last-name]")
                                      )
input_address = driver.find_element(By.CSS_SELECTOR,
                                    (".form-control[name=address]")
                                    )
input_zip_code = driver.find_element(By.CSS_SELECTOR,
                                     (".form-control[name=zip-code]")
                                     )
input_city = driver.find_element(By.CSS_SELECTOR,
                                 (".form-control[name=city]")
                                 )
input_country = driver.find_element(By.CSS_SELECTOR,
                                    (".form-control[name=country]")
                                    )
input_email = driver.find_element(By.CSS_SELECTOR,
                                  (".form-control[name=e-mail]")
                                  )
input_phone = driver.find_element(By.CSS_SELECTOR,
                                  (".form-control[name=phone]")
                                  )
input_job_position = driver.find_element(By.CSS_SELECTOR,
                                         (".form-control[name=job-position]")
                                         )
input_company = driver.find_element(By.CSS_SELECTOR,
                                    (".form-control[name=company]")
                                    )
btn_sumbit = driver.find_element(By.CSS_SELECTOR,
                                 ("button.btn.btn-outline-primary.mt-3")
                                 )

input_first_name.send_keys("Иван")
input_last_name.send_keys("Петров")
input_address.send_keys("Ленина, 55-3")
input_zip_code.send_keys("")
input_city.send_keys("Москва")
input_country.send_keys("Россия")
input_email.send_keys("test@skypro.com")
input_phone.send_keys("+7985899998787")
input_job_position.send_keys("QA")
input_company.send_keys("SkyPro")
btn_sumbit.click()

first_name_color = driver.find_element(By.CSS_SELECTOR,
                                       "div.alert#first-name")\
                                       .value_of_css_property(
                                        "background-color")
last_name_color = driver.\
    find_element(By.CSS_SELECTOR,
                 "div.alert.py-2#last-name")\
    .value_of_css_property("background-color")
address_color = driver.find_element(By.CSS_SELECTOR,
                                    'div.alert.py-2#address')\
                                     .value_of_css_property("background-color")
city_color = driver.find_element(By.CSS_SELECTOR,
                                 'div.alert.py-2#city')\
                                 .value_of_css_property("background-color")
country_color = driver.find_element(By.CSS_SELECTOR,
                                    'div.alert.py-2#country')\
                                    .value_of_css_property("background-color")
email_color = driver.find_element(By.CSS_SELECTOR,
                                  'div.alert.py-2#e-mail')\
                                  .value_of_css_property("background-color")
phone_color = driver.find_element(By.CSS_SELECTOR,
                                  'div.alert.py-2#phone')\
                                  .value_of_css_property("background-color")
job_position_color = driver.find_element(By.CSS_SELECTOR,
                                         'div.alert.py-2#job-position')\
                            .value_of_css_property("background-color")
company_color = driver.find_element(By.CSS_SELECTOR,
                                    'div.alert.py-2#company')\
                                    .value_of_css_property("background-color")


zip_color = driver.find_element(By.CSS_SELECTOR,
                                "#zip-code.alert-danger")\
                                .value_of_css_property("background-color")


red_color = 'rgba(248, 215, 218, 1)'
green_color = "rgba(209, 231, 221, 1)"


print(zip_color)
print(first_name_color, last_name_color)

colors = [first_name_color, last_name_color, address_color,
          city_color, country_color, email_color, phone_color,
          job_position_color, company_color]


def test_invalid_zip():
    for color in colors:
        assert color == green_color

    assert zip_color == red_color
    driver.close()
