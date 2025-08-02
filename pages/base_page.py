import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_locators = BasePageLocators()  # Добавляем общие локаторы

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return self

    @allure.step("Ввести текст '{text}' в поле {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Проверить видимость элемента {locator}")
    def is_element_visible(self, locator, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).is_displayed()
        except:
            return False

    @allure.step("Проверить явное ожидание списка элементов {locator}")
    def wait_for_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Проверить явное ожидание элемента {locator}")
    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Скролл к элементу")
    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 3).until(
            lambda d: element.is_displayed()
        )
        return self

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click(self.base_locators.SCOOTER_LOGO)
        return self

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(self.base_locators.YANDEX_LOGO)
        return self

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return self

    @allure.step("Закрыть вкладку и вернуться на основную вкладку")
    def close_and_return_to_main_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return self

    @allure.step("Подождать URL содержащую: '{text}'")
    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text)
        )
        return self

