import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть страницу qa-scooter")
    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
        return self

    @allure.step("Принять куки")
    def accept_cookies(self):
        try:
            self.click(BasePageLocators.COOKIE_BUTTON, timeout=5)
        except:
            pass
        return self

    @allure.step('Начать заказ с верхней кнопки "Заказать"')
    def start_order_from_top_button(self):
        self.click(MainPageLocators.TOP_ORDER_BUTTON)
        from pages.order_page import OrderPage
        return OrderPage(self.driver)

    @allure.step('Начать заказ с нижней кнопки "Заказать"')
    def start_order_from_bottom_button(self):
        element = self.wait_for_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)
        from pages.order_page import OrderPage
        return OrderPage(self.driver)

    @allure.step('Проскроллить к разделу FAQ')
    def scroll_to_faq_section(self):
        from pages.faq_page import FaqPage
        faq_page = FaqPage(self.driver)
        faq_section = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(faq_page.locators.FAQ_SECTION)
        )
        self.scroll_to_element(faq_section)
        return faq_page

