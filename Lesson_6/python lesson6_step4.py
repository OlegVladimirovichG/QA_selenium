from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запускаем браузер
browser = webdriver.Chrome()

# Открываем нужную страницу
browser.get("http://suninjuly.github.io/simple_form_find_task.html")  # <-- тут подставь свою страницу

try:
    # Находим поля и заполняем их
    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # Нажимаем кнопку Submit
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
