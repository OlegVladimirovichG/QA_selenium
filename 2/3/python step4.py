from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    # Нажимаем кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    # Находим поля и заполняем их
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем кнопку Submit
    browser.find_element(By.CLASS_NAME, "btn").click()

finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
