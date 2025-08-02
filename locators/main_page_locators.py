from selenium.webdriver.common.by import By


class MainPageLocators:
    TOP_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class, 'Header_Nav')]]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'UltraBig')]")