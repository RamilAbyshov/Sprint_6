from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Первая страница заказа
    NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Адрес: куда привезти')]")
    METRO_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    PHONE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Телефон: на него позвонит')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница заказа
    DATE_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Когда привезти самокат')]")
    TODAY_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day--today')]")
    TOMORROW_DATE = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='{}']")
    RENTAL_DROPDOWN = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTION = (By.XPATH, "//div[text()='{}']")
    BLACK_COLOR = (By.ID, "black")
    GREY_COLOR = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and ancestor::div[contains(@class, 'Order_Buttons')]]")

    # Модальное окно подтверждения
    CONFIRM_MODAL = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Заголовки форм
    CUSTOMER_FORM_TITLE = (By.XPATH, "//div[text()='Для кого самокат']")
    RENTAL_FORM_TITLE = (By.XPATH, "//div[text()='Про аренду']")