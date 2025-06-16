from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    service = Service(executable_path=ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get(link)

    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)

    calc = str(x + y)

    # Находим поля и заполняем их
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(calc)

    # Нажимаем кнопку Submit
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()


finally:
    # Ждём, чтобы увидеть результат (можно убрать после отладки)
    time.sleep(5)
    browser.quit()
