from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def calc(a):
    return str(math.log(abs(12 * math.sin(int(a)))))


try:
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку Submit
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    # Находим поля и заполняем их
    browser.find_element(By.ID, "answer").send_keys(y)

    # Нажимаем кнопку Submit
    browser.find_element(By.ID, "solve").click()

finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
