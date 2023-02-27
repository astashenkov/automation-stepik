import math
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.parametrize('link', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
])
def test_authorization(browser, link):

    browser.get(link)
    login_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'ember33')))
    login_button.click()

    browser.find_element(By.CSS_SELECTOR, '[name="login"]').send_keys('Your email')
    browser.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys('Your password')
    browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    time.sleep(2)

    answer_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR,
            '.ember-text-area.ember-view.textarea.string-quiz__textarea'
        ))
    )

    if answer_input.get_attribute('disabled'):
        browser.find_element(By.CSS_SELECTOR, '.again-btn.white').click()
        time.sleep(3)

        answer_input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                '.ember-text-area.ember-view.textarea.string-quiz__textarea'
            ))
        )

    answer = math.log(int(time.time()))
    answer_input.send_keys(answer)
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()

    result = WebDriverWait(browser, 30).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'p.smart-hints__hint')
        )
    ).text

    assert result == 'Correct!', f'"{result}"'
