import pytest
import allure

from pages.faq_page import FaqPage
from src.data import TestData


@allure.suite("Тесты раздела FAQ")
class TestFAQ:
    @allure.feature("Проверка вопросов-ответов")
    @allure.title("Проверка отображения ответа на вопрос FAQ с индексом {question_index}")
    @pytest.mark.parametrize('question_index,expected_answer', TestData.FaqData.FAQ)
    def test_faq_questions(self, driver, main_page, question_index, expected_answer):
        faq_page = FaqPage(driver)
        faq_page = faq_page.scroll_to_faq_section()
        faq_page.click_question(question_index)
        faq_page.verify_answer_visible(question_index)
        faq_page.verify_answer_text(question_index, expected_answer)