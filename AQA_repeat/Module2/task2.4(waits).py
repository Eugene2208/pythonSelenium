import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    waiter = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button = browser.find_element(By.ID, 'book')
    button.click()
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    button = browser.find_element(By.ID, 'solve')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
