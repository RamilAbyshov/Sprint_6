import pytest
import allure
from src.data import TestData


@allure.suite("Тесты раздела FAQ")
class TestFAQ:
    @allure.feature("Проверка вопросов-ответов")
    @pytest.mark.parametrize('question_index,expected_answer', TestData.FaqData.FAQ)
    def test_faq_questions(self, main_page, question_index, expected_answer):
        with allure.step(f"Проверка вопроса #{question_index}"):
            faq_page = main_page.scroll_to_faq_section()

            with allure.step("Клик по вопросу"):
                faq_page.click_question(question_index)

            with allure.step("Проверка видимости ответа"):
                faq_page.verify_answer_visible(question_index)

            with allure.step("Проверка текста ответа"):
                faq_page.verify_answer_text(question_index, expected_answer)