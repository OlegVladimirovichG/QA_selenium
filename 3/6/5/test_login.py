import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ссылки для параметризации
links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

# Собираем части "секретного сообщения"
collected_feedback = []

@pytest.mark.parametrize("link", links)
def test_login_click(link, browser):
    browser.get(link)

    # Логин
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "ember479"))).click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "id_login_email"))).send_keys("hankat@mail.ru")
    browser.find_element(By.ID, "id_login_password").send_keys("Jktu24111988")
    browser.find_element(By.CLASS_NAME, "sign-form__btn").click()

    # Расчёт ответа
    answer = math.log(int(time.time()))

    # Вводим ответ
    textarea = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea"))
    )
    textarea.clear()
    textarea.send_keys(answer)

    # Отправляем
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()

    # Проверка ответа
    feedback = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )
    actual_text = feedback.text
    expected_text = "Correct!"

    if actual_text != expected_text:
        collected_feedback.append(actual_text)

    assert actual_text == expected_text, f"Expected '{expected_text}', got '{actual_text}'"


# Этот хук вызывается в конце всех тестов
def pytest_sessionfinish(session, exitstatus):
    if collected_feedback:
        print("\n\n🎯 Секретное сообщение:")
        print("".join(collected_feedback))
