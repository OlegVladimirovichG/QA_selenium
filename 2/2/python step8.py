import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("https://suninjuly.github.io/file_input.html")


    # Находим поля и заполняем их
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")

    # Находим поля и заполняем их
    browser.find_element(By.NAME, "lastname").send_keys("Ivanov")

    browser.find_element(By.NAME, "email").send_keys("<EMAIL>")

    text_file = browser.find_element(By.ID, "file")
    file_path = os.path.abspath('file.txt')
    text_file.send_keys(file_path)

    # Нажимаем кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()



finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
