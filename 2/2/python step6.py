from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("https://SunInJuly.github.io/execute_script.html")

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    # Находим поля и заполняем их
    browser.find_element(By.ID, "answer").send_keys(y)

    # Находим поля и заполняем их
    browser.find_element(By.ID, "robotCheckbox").click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Нажимаем кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()



finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
