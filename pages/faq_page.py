import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage
from locators.faq_page_locators import FaqPageLocators


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FaqPageLocators()

    @allure.step("Кликнуть по вопросу номер с индексом: {index}")
    def click_question(self, index):
        questions = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators.FAQ_QUESTIONS)
        )
        question = questions[index]
        self.scroll_to_element(question)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(question)
        ).click()
        return self

    @allure.step("Проверить видимость ответа с индексом: {index}")
    def verify_answer_visible(self, index):
        answers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators.FAQ_ANSWERS)
        )
        assert answers[index].is_displayed(), f"Ответ {index} не отображается"
        return self

    @allure.step("Проверить текст ответа с индексом: {index}")
    def verify_answer_text(self, index, expected_text):
        answers = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.locators.FAQ_ANSWERS)
        )
        answer_text = answers[index].text
        assert expected_text in answer_text, (
            f"Ожидался текст: '{expected_text}'\nПолучен: '{answer_text}'"
        )
        return self