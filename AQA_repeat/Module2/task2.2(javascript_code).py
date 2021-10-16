import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # browser.execute_script("document.title='Script executing';alert('Robots at work');")
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    radio_btm=browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_btm)
    radio_btm.click()
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # browser.execute_script("window.scrollBy(0, 100);")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
