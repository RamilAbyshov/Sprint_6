import pytest
import allure
from pages.order_page import OrderPage
from src.data import TestData

@allure.suite("Тесты оформления заказа")
class TestOrderFlow:
    @allure.feature("Оформление заказа через верхнюю кнопку")
    @allure.title("Проверка заказа через верхнюю кнопку")
    def test_order_from_top_button(self, driver, main_page):
        test_case = TestData.OrderData.PERSONAL_INFO[0]  # Данные для верхней кнопки

        main_page.start_order_from_top_button()
        order_page = OrderPage(main_page.driver)

        order_page.fill_customer_info(**test_case["customer"])
        order_page.fill_rental_info(**test_case["rental"])
        order_page.confirm_order()

        assert order_page.is_order_confirmed()

    @allure.feature("Оформление заказа через нижнюю кнопку")
    @allure.title("Проверка заказа через нижнюю кнопку")
    def test_order_from_bottom_button(self, driver, main_page):
        test_case = TestData.OrderData.PERSONAL_INFO[1]  # Данные для нижней кнопки

        main_page.start_order_from_bottom_button()
        order_page = OrderPage(main_page.driver)

        order_page.fill_customer_info(**test_case["customer"])
        order_page.fill_rental_info(**test_case["rental"])
        order_page.confirm_order()
