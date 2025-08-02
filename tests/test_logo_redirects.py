import allure
from src.data import TestData


@allure.suite("Тесты редиректов по логотипам")
class TestLogoRedirects:
    @allure.feature("Редирект логотипа Самоката")
    def test_scooter_logo_redirect(self, main_page, driver):
        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить URL после редиректа"):
            main_page.wait_for_url_contains(TestData.LogoRedirectData.SCOOTER_EXPECTED_URL)
            assert TestData.LogoRedirectData.SCOOTER_EXPECTED_URL in driver.current_url

    @allure.feature("Редирект логотипа Яндекса")
    def test_yandex_logo_redirect(self, main_page, driver):
        with allure.step("Запомнить текущую вкладку"):
            main_window = driver.current_window_handle

        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новую вкладку"):
            main_page.switch_to_new_tab()

        with allure.step("Проверить URL Дзена"):
            main_page.wait_for_url_contains(TestData.LogoRedirectData.YANDEX_EXPECTED_URL)
            assert TestData.LogoRedirectData.YANDEX_EXPECTED_URL in driver.current_url

        with allure.step("Закрыть вкладку и вернуться"):
            driver.close()
            driver.switch_to.window(main_window)