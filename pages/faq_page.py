import allure
from .base_page import BasePage
from locators.faq_page_locators import FaqPageLocators


class FaqPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FaqPageLocators()

    @allure.step("Кликнуть по вопросу номер {index}")
    def click_question(self, index):
        questions = self.wait_for_all_elements_visible(self.locators.FAQ_QUESTIONS)
        question = questions[index]
        self.scroll_to_element(question)
        self.wait_for_element_clickable(question).click()
        return self

    @allure.step("Проверить видимость ответа {index}")
    def verify_answer_visible(self, index):
        answers = self.wait_for_all_elements_visible(self.locators.FAQ_ANSWERS)
        assert answers[index].is_displayed(), f"Ответ {index} не отображается"
        return self

    @allure.step("Проверить текст ответа {index}")
    def verify_answer_text(self, index, expected_text):
        answers = self.wait_for_all_elements_visible(self.locators.FAQ_ANSWERS)
        actual_text = answers[index].text
        assert expected_text in actual_text, (
            f"Ожидался текст: '{expected_text}'\nПолучен: '{actual_text}'"
        )
        return self

    @allure.step('Проскроллить к разделу FAQ')
    def scroll_to_faq_section(self):
        faq_section = self.wait_for_element(self.locators.FAQ_SECTION)
        self.scroll_to_element(faq_section)
        return self
