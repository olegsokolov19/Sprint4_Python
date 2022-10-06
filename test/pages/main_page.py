from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

from .locators import MainPageLocators


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    @allure.step('Ожидание загрузки элемента')
    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(element))

    @allure.step('Прокрутка до блока с вопросами (FAQ)')
    def scroll_into_view_FAQ_elements(self):
        accordion_elements = self.driver.find_element(*MainPageLocators.LOCATOR_ACCORDION_ELEMENTS)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_elements)
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(MainPageLocators.LOCATOR_ACCORDION_ELEMENTS))

    @allure.step('Нажатие по кнопке "Да, все привыкли" (закрытие плашки куки)')
    def click_button_cookie(self):
        button_cookie = self.driver.find_element(*MainPageLocators.LOCATOR_BUTTON_COOKIE)
        if ec.visibility_of_element_located(button_cookie):
            button_cookie.click()

    @allure.step('Нажатие по вопросу, чтобы раскрыть его')
    def click_question(self, question):
        LOCATOR_QUESTION = [By.XPATH, f".//div[@data-accordion-component='AccordionItemButton' and contains(text(), "
                                          f"'{question}')]"]
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(LOCATOR_QUESTION))
        self.driver.find_element(*LOCATOR_QUESTION).click()

    @allure.step('Получение текста ответа на подаваемый на вход вопрос')
    def get_text_answer(self, question):
        LOCATOR_ANSWER = [By.XPATH,
                              f".//div[@data-accordion-component='AccordionItem'] / "
                              f".//div[@data-accordion-component='AccordionItemButton' and contains(text(), '{question}')] "
                              f"/ parent::* / ../div[@data-accordion-component='AccordionItemPanel']"]
        WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located(LOCATOR_ANSWER))
        return self.driver.find_element(*LOCATOR_ANSWER).text

    @allure.step('Кликнуть по вопросу и получить его ответ')
    def click_answer_and_get_question(self, question):
        self.click_question(question)
        return self.get_text_answer(question)

    @allure.step('Нажатие по кнопке "Яндекс" в шапке страницы')
    def click_on_yandex_button_in_the_header_of_page(self):
        self.driver.find_element(*MainPageLocators.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).click()

    @allure.step('Нажатие по кнопке "Самокат" в шапке страницы')
    def click_on_yandex_button_in_the_header_of_page(self):
        self.driver.find_element(*MainPageLocators.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).click()

    @allure.step('Проверка ссылки в кнопке "Яндекс" в шапке страницы')
    def check_link_in_yandex_button_in_the_header_of_page(self):
        link = self.driver.find_element(*MainPageLocators.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).get_attribute('href')

        if link is None or len(link) == 0 or not ("yandex.ru" in link):
            return None
        else:
            self.driver.find_element(*MainPageLocators.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).click()
            return True

    @allure.step('Проверка ссылки в кнопке "Яндекс" в шапке страницы')
    def check_link_in_scooter_button_in_the_header_of_page(self):
        link = self.driver.find_element(*MainPageLocators.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).get_attribute('href')

        if link is None or len(link) == 0 or not ("qa-scooter.praktikum-services.ru" in link):
            return None
        else:
            self.driver.find_element(*MainPageLocators.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).click()
            return True
