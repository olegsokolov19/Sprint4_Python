from selenium.webdriver.support import expected_conditions as ec
import allure
from selenium.webdriver.support.wait import WebDriverWait
import re

from .locators import OrderPageLocators
from .locators import MainPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/order/"

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def go_to_main_page(self):
        scooter_button = MainPageLocators.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(scooter_button))
        self.driver.find_element(*scooter_button).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.LOCATOR_HOME_HEADER))

    @allure.step('Заполнение поля "Имя"')
    def set_field_name(self, name):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_NAME).send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_field_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_SURNAME).send_keys(surname)

    @allure.step('Заполнение поля "Адресс"')
    def set_field_address(self, address):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_ADDRESS).send_keys(address)

    @allure.step('Заполнение поля "Метро"')
    def set_field_metro(self, metro):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_METRO).send_keys(metro)
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(OrderPageLocators.LOCATOR_BUTTON_WITH_METRO_STATION_NAME))
        self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_WITH_METRO_STATION_NAME).click()

    @allure.step('Заполнение поля "Телефон"')
    def set_field_phone(self, phone):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_PHONE).send_keys(phone)

    @allure.step('Нажатие по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_NEXT).click()

    @allure.step('Нажатие по кнопке "Заказать" в шапке страницы')
    def click_button_order_in_header(self):
        self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_ORDER).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(OrderPageLocators.LOCATOR_BUTTON_NEXT))

    @allure.step('Нажатие по кнопке "Заказать" внизу страницы')
    def click_button_order_at_the_bottom_of_page(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM))
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(OrderPageLocators.LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM))
        self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM).click()

    @allure.step('Выбор даты доставки')
    def select_date_to_delivery(self, date):
        self.driver.find_element(*OrderPageLocators.LOCATOR_INACTIVE_FIELD_SELECT_A_DELIVERY_TIME).send_keys(date)
        self.driver.find_element(*OrderPageLocators.LOCATOR_ACTIVE_FIELD_SELECT_A_DELIVERY_TIME).click()

    @allure.step('Заполнение поля "Срок аренды"')
    def select_rental_period(self, day_count):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(OrderPageLocators.LOCATOR_DROPDOWN_MENU_WITH_RENTAL_PERIOD))
        self.driver.find_elements(*OrderPageLocators.LOCATOR_DROPDOWN_MENU_WITH_RENTAL_PERIOD)[day_count - 1].click()

    @allure.step('Выбор цвета самоката')
    def select_scooter_color(self, color):
        if color == 'black':
            self.driver.find_elements(*OrderPageLocators.LOCATOR_SCOOTER_COLORS_SELECTION)[0].click()
        elif color == 'grey':
            self.driver.find_elements(*OrderPageLocators.LOCATOR_SCOOTER_COLORS_SELECTION)[1].click()
        elif color == 'grey and black' or color == 'black and grey':
            self.driver.find_elements(*OrderPageLocators.LOCATOR_SCOOTER_COLORS_SELECTION)[0].click()
            self.driver.find_elements(*OrderPageLocators.LOCATOR_SCOOTER_COLORS_SELECTION)[1].click()

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_field_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.LOCATOR_FIELD_COMMENT).send_keys(comment)

    @allure.step('Нажатие по кнопке "Заказать" после заполнения всех обязательных полей')
    def click_button_place_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(OrderPageLocators.LOCATOR_ORDER_BUTTON))
        self.driver.find_element(*OrderPageLocators.LOCATOR_ORDER_BUTTON).click()

    @allure.step('Нажатие по кнопке "Да" в окне "Хотите оформить заказ?"')
    def click_button_yes_in_form_place_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(OrderPageLocators.LOCATOR_BUTTON_YES_IN_FORM_WANT_PLACE_ORDER))
        self.driver.find_element(*OrderPageLocators.LOCATOR_BUTTON_YES_IN_FORM_WANT_PLACE_ORDER).click()

    @allure.step('Получение окна об успешном оформлении заказа')
    def get_successful_create_order_message(self):
        message = self.driver.find_element(*OrderPageLocators.LOCATOR_MESSAGE_ABOUT_SUCCESSFUL_ORDER_PROCESSING).text
        return re.search("[0-9]+", message)

    @allure.step('Заполнение всех обязательных полей для оформления заказа')
    def fill_all_required_fields(self, name, surname, address, metro, phone, date, rental, color, comment=None):
        self.set_field_name(name)
        self.set_field_surname(surname)
        self.set_field_address(address)
        self.set_field_metro(metro)
        self.set_field_phone(phone)
        self.click_next_button()
        self.select_date_to_delivery(date)
        self.select_rental_period(rental)
        self.select_scooter_color(color)
        if comment is not None:
            self.set_field_comment(comment)
