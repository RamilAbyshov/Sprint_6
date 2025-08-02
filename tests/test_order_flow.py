import pytest
import allure

from src.data import TestData


@allure.suite("Тесты оформления заказа")
class TestOrderFlow:
    @allure.feature("Оформление заказа")
    @pytest.mark.parametrize("test_case", TestData.OrderData.PERSONAL_INFO,
                             ids=["Top button + today", "Bottom button + tomorrow"])
    def test_order_flow(self, main_page, test_case):
        with allure.step("Инициализация заказа"):
            if test_case["button"] == "top":
                order_page = main_page.start_order_from_top_button()
            else:
                order_page = main_page.start_order_from_bottom_button()

        with allure.step("Заполнение данных клиента"):
            order_page.fill_customer_info(**test_case["customer"])

        with allure.step("Заполнение данных аренды"):
            order_page.fill_rental_info(**test_case["rental"])

        with allure.step("Подтверждение заказа"):
            order_page.confirm_order()

        with allure.step("Проверка успешного оформления"):
            assert order_page.is_order_confirmed()