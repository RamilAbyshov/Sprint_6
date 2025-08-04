import allure
from src.data import TestData
from src.config import Config

@allure.suite("Тесты редиректов по логотипам")
class TestLogoRedirects:
    @allure.feature("Редирект логотипа Самоката")
    @allure.title("Проверка редиректа на основную страницу при клике лого Самоката")
    def test_scooter_logo_redirect(self, main_page, driver):
        main_page.click_scooter_logo()
        main_page.wait_for_url_contains(Config.BASE_URL)
        assert Config.BASE_URL in main_page.get_current_url()

    @allure.feature("Редирект логотипа Яндекса")
    @allure.title("Проверка редиректа на страницу Дзена при клике лого Яндекса")
    def test_yandex_logo_redirect(self, main_page, driver):
        main_window = main_page.get_current_window()
        main_page.click_yandex_logo()
        main_page.switch_to_new_tab()
        main_page.wait_for_url_contains(TestData.LogoRedirectData.YANDEX_EXPECTED_URL)
        assert TestData.LogoRedirectData.YANDEX_EXPECTED_URL in main_page.get_current_url()

        main_page.close_current_window()
        main_page.switch_to_window(main_window)