import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)
    browser.execute_script("document.getElementsByTagName('button')[0].classList.remove('trollface');")
    button = browser.find_element(By.CLASS_NAME, 'btn').get_attribute()
    button.click()
    new_window = browser.window_handles[1]  # имя новой вкладки
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="Submit"]')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
