from selenium.webdriver.common.by import By

class FaqPageLocators:
    FAQ_SECTION = (By.CSS_SELECTOR, "[data-accordion-component='Accordion']")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemButton']")
    FAQ_ANSWERS = (By.CSS_SELECTOR, "[data-accordion-component='AccordionItemPanel']")