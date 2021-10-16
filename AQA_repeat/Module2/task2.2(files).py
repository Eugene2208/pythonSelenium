import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    firstname = browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
    firstname.send_keys("firstname")
    lastname = browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
    lastname.send_keys("lastname")
    email = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
    email.send_keys("email")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)
    button = browser.find_element(By.CLASS_NAME,'btn')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла