import pytest
import time

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.locators import ProductPageLocators


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        new_user = str(time.time())
        page.register_new_user(new_user + '@fakemail.org', new_user)
        page.should_be_authorized_user()
        time.sleep(20)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()

        product_page.add_to_basket()
        product_page.solve_quiz_and_get_code()

        product_price = product_page.get_current_product_price()
        product_title = product_page.get_current_product_title()

        assert product_price == product_page.get_added_to_basket_product_price(), f'Different product price! {link}'
        assert product_title == product_page.get_added_to_basket_product_title(), f'Different product title! {link}'

    @pytest.mark.xfail
    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_to_basket()
        assert product_page.is_not_element_present(
            *ProductPageLocators.SUCCESS_ADDED_MESSAGE
        ), 'Success message is presents on the page but should not be.'


@pytest.mark.need_review
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
    "?promo=offer9", ])
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


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_not_element_present(
        *ProductPageLocators.SUCCESS_ADDED_MESSAGE
    ), 'Success message is presents on the page but should not be.'


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    assert product_page.is_disappeared(
        *ProductPageLocators.SUCCESS_ADDED_MESSAGE
    ), 'Success message is presents on the page but should not be.'


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.open()
    import time
    time.sleep(10)
    basket_page.check_is_empty_basket()
    basket_page.check_empty_basket_message()
