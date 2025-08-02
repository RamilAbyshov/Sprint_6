from selenium.webdriver.common.by import By


class BasePageLocators:
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    # Логотипы
    YANDEX_LOGO = (By.CSS_SELECTOR, "[href*='yandex.ru'] img")
    SCOOTER_LOGO = (By.CSS_SELECTOR, "[href='/'] img")