import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()

    # ✅ Отключаем менеджер паролей
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    # ✅ Дополнительные полезные флаги
    options.add_argument("--disable-notifications")     # блокируем уведомления
    options.add_argument("--disable-popup-blocking")    # блокируем всплывающие окна
    options.add_argument("--incognito")                 # режим инкогнито (без сохранения кэша и паролей)
    options.add_argument("--start-maximized")           # на весь экран

    # ✅ Опционально: без GUI (если нужно запускать на сервере/CI)
    # options.add_argument("--headless=new")             # для Chrome 109+
    print("\nstart browser for test..")
    # ✅ Создаём драйвер
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()