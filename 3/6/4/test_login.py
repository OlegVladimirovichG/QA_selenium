import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "https://stepik.org/lesson/236895/step/1"

def test_login_click(browser):
    browser.get(link)

    # Явное ожидание и клик по кнопке входа
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "ember479"))).click()

    # Ввод email и пароля
    WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))).send_keys("hankat@mail.ru")

    browser.find_element(By.ID, "id_login_password").send_keys("Jktu24111988")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    # Ждём, пока появится поле для ответа
    textarea = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )
    textarea.send_keys("test input")

    # Ждём и нажимаем кнопку отправки
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()

    # Подтверждение (можно проверить сообщение об успешной отправке)
    time.sleep(5)  # или ожидание результата