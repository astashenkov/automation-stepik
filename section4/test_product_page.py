import time

import pytest

from .pages.product_page import ProductPage

@pytest.mark.parametrize('promo', [
    "?promo=offer0",
    "?promo=offer1",
    "?promo=offer2",
    "?promo=offer3",
    "?promo=offer4",
    "?promo=offer5",
    "?promo=offer6",
    pytest.param("?promo=offer7", marks=pytest.mark.xfail),
    "?promo=offer8",
    "?promo=offer9",])
def test_guest_can_add_product_to_basket(browser, promo):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

    product_price = product_page.get_current_product_price()
    product_title = product_page.get_current_product_title()

    assert product_price == product_page.get_added_to_basket_product_price(), f'Different product price! {link}'
    assert product_title == product_page.get_added_to_basket_product_title(), f'Different product title! {link}'
