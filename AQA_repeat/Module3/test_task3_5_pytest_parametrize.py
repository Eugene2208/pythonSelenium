import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.implicitly_wait(5)
    browser.get(link)
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, "textarea[spellcheck]").send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, "button[class='submit-submission']").click()
    actual_text = browser.find_element(By.CSS_SELECTOR, "pre[class]")
    assert actual_text.text == "Correct!", "Should be equal"
