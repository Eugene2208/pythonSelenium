from selenium.webdriver.common.by import By


def test_to_find_the_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    add_to_basket_button = browser.find_elements(By.XPATH, '//form[@id="add_to_basket_form"]/button')

    assert add_to_basket_button != [], f'Кнопка отсутствует на странице'