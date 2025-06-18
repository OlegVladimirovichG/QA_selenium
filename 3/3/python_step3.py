import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("Ivanovich@krootoi.net")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input").send_keys("1234567890")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input").send_keys("Питер!")

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Ivanov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("Ivanovich@krootoi.net")
        browser.find_element(By.CSS_SELECTOR, ".second_block .first_class input").send_keys("1234567890")
        browser.find_element(By.CSS_SELECTOR, ".second_block .second_class input").send_keys("Питер!")

        # Отправляем заполненную форму
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        browser.quit()


if __name__ == '__main__':
    unittest.main()
