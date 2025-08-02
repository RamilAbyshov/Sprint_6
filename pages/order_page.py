from datetime import datetime, timedelta

import allure
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить данные клиента")
    def fill_customer_info(self, name, last_name, address, metro, phone):
        self.wait_for_element(OrderPageLocators.CUSTOMER_FORM_TITLE)

        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self._select_metro_station(metro)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)
        return self

    @allure.step("Заполнить данные аренды")
    def fill_rental_info(self, date_option="today", rental_period="сутки", color="black", comment=""):
        self.wait_for_element(OrderPageLocators.RENTAL_FORM_TITLE)

        self._select_delivery_date(date_option)
        self._select_rental_period(rental_period)
        self._select_scooter_color(color)
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_BUTTON)
        return self

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_BUTTON)
        return self

    @allure.step("Проверить что заказ оформлен")
    def is_order_confirmed(self):
        return self.is_element_visible(OrderPageLocators.SUCCESS_MESSAGE, timeout=20)

    @allure.step('Выбрать станцию метро "{station_name}"')
    def _select_metro_station(self, station_name):
        self.click(OrderPageLocators.METRO_INPUT)
        self.send_keys(OrderPageLocators.METRO_INPUT, station_name)
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).send_keys(Keys.DOWN, Keys.RETURN)

    @allure.step("Выбрать дату доставки")
    def _select_delivery_date(self, date_option):
        self.click(OrderPageLocators.DATE_INPUT)

        if date_option == "today":
            locator = OrderPageLocators.TODAY_DATE
        elif date_option == "tomorrow":
            tomorrow_day = (datetime.now() + timedelta(days=1)).day
            locator = (OrderPageLocators.TOMORROW_DATE[0],
                       OrderPageLocators.TOMORROW_DATE[1].format(tomorrow_day))
        else:
            raise ValueError(f"Unknown date option: {date_option}")

        self.click(locator)
        self.click(OrderPageLocators.RENTAL_FORM_TITLE)

    @allure.step("Выбрать срок аренды")
    def _select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_DROPDOWN)
        rental_option = (OrderPageLocators.RENTAL_OPTION[0],
                         OrderPageLocators.RENTAL_OPTION[1].format(period))
        self.click(rental_option)

    @allure.step("Выбрать {color} цвет самоката")
    def _select_scooter_color(self, color):
        if color == "black":
            self.click(OrderPageLocators.BLACK_COLOR)
        elif color == "grey":
            self.click(OrderPageLocators.GREY_COLOR)
        else:
            raise ValueError(f"Unknown color: {color}")