from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Находим поля и заполняем их
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox").click()

    radio_robor_rule = browser.find_element(By.ID, "robotsRule").click()

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
