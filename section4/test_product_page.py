import pytest

from .pages.product_page import ProductPage

@pytest.mark.parametrize('link', [
    'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear',
    'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()

    product_price = product_page.get_current_product_price()
    product_title = product_page.get_current_product_title()

    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    assert product_price == product_page.get_added_to_basket_product_price(), 'Different product price!'
    assert product_title in product_page.get_add_to_basket_alert_message(), 'Different product title!'
