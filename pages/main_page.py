import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from src.config import Config


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators()

    @allure.step("Открыть страницу qa-scooter")
    def open(self):
        return self.open_url(Config.BASE_URL)

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

    @allure.step('Начать заказ с нижней кнопки "Заказать"')
    def start_order_from_bottom_button(self):
        element = self.wait_for_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step('Проскроллить к разделу FAQ')
    def scroll_to_faq_section(self):
        from pages.faq_page import FaqPage
        faq_page = FaqPage(self.driver)
        faq_section = self.wait_for_element(faq_page.locators.FAQ_SECTION)
        self.scroll_to_element(faq_section)
        return faq_page

