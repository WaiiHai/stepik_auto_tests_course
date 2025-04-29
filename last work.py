import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


# Инициализация драйвера (укажите путь к вашему chromedriver)
browser = webdriver.Chrome(service=Service(ChromeDriverManager(driver_version="135.0.7049.114").install()))

link = "https://suninjuly.github.io/explicit_wait2.html"
browser.get(link)
try:
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.TAG_NAME, 'button').click()
    value = browser.find_element(By.ID, 'input_value').text
    t = math.log(abs(12*math.sin(int(value))))
    browser.find_element(By.ID,'answer').send_keys(t)
    browser.find_element(By.ID, 'solve').click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()