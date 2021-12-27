import unittest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def scenario(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        field_name = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
        field_name.send_keys('Name')
        field_last_name = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
        field_last_name.send_keys('Name')
        field_email = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
        field_email.send_keys('email')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    finally:
        # закрываем браузер после всех манипуляций
        browser.quit()
        return welcome_text


class TestUnit(unittest.TestCase):

    def test_abs1(self):
        exp_res = "Congratulations! You have successfully registered!"
        act_res = scenario("http://suninjuly.github.io/registration1.html")
        self.assertEqual(exp_res, act_res, "Should be equal")

    def test_abs2(self):
        exp_res = "Congratulations! You have successfully registered!"
        act_res = scenario("http://suninjuly.github.io/registration2.html")
        self.assertEqual(exp_res, act_res, "Should be equal")


if __name__ == "__main__":
    unittest.main()
