from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import allure
import re


class MainPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    LOCATOR_ACCORDION_ELEMENTS = [By.CSS_SELECTOR, "div.accordion__item"]

    LOCATOR_FIRST_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-0']"]
    LOCATOR_FIRST_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-0']"]

    LOCATOR_SECOND_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-1']"]
    LOCATOR_SECOND_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-1']"]

    LOCATOR_THIRD_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-2']"]
    LOCATOR_THIRD_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-2']"]

    LOCATOR_FOURTH_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-3']"]
    LOCATOR_FOURTH_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-3']"]

    LOCATOR_FIFTH_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-4']"]
    LOCATOR_FIFTH_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-4']"]

    LOCATOR_SIXTH_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-5']"]
    LOCATOR_SIXTH_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-5']"]

    LOCATOR_SEVENTH_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-6']"]
    LOCATOR_SEVENTH_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-6']"]

    LOCATOR_EIGHTH_QUESTION = [By.XPATH, ".//div[@id='accordion__heading-7']"]
    LOCATOR_EIGHTH_ANSWER = [By.XPATH, ".//div[@id='accordion__panel-7']"]

    LOCATOR_BUTTON_COOKIE = [By.CLASS_NAME, "App_CookieButton__3cvqF"]

    LOCATOR_YANDEX_BUTTON_IN_THE_HEADER = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    @allure.step('Ожидание загрузки элемента')
    def wait_for_load_element(self, element):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(element))

    @allure.step('Прокрутка до блока с вопросами (FAQ)')
    def scroll_into_view_FAQ_elements(self):
        accordion_elements = self.driver.find_element(*self.LOCATOR_ACCORDION_ELEMENTS)
        self.driver.execute_script("arguments[0].scrollIntoView();", accordion_elements)

    @allure.step('Нажатие по кнопке "Да, все привыкли" (закрытие плашки куки)')
    def click_button_cookie(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(self.LOCATOR_BUTTON_COOKIE))
        self.driver.find_element(*self.LOCATOR_BUTTON_COOKIE).click()

    @allure.step('Получение текста ответа на первый вопрос')
    def get_text_first_answer(self):
        self.click_button_cookie()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_FIRST_QUESTION))
        self.driver.find_element(*self.LOCATOR_FIRST_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_FIRST_ANSWER)

        return self.driver.find_element(*self.LOCATOR_FIRST_ANSWER).text

    @allure.step('Получение текста ответа на второй вопрос')
    def get_text_second_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_SECOND_QUESTION))
        self.driver.find_element(*self.LOCATOR_SECOND_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_SECOND_ANSWER)

        return self.driver.find_element(*self.LOCATOR_SECOND_ANSWER).text

    @allure.step('Получение текста ответа на третий вопрос')
    def get_text_third_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_THIRD_QUESTION))
        self.driver.find_element(*self.LOCATOR_THIRD_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_THIRD_ANSWER)

        return self.driver.find_element(*self.LOCATOR_THIRD_ANSWER).text

    @allure.step('Получение текста ответа на четвертый вопрос')
    def get_text_fourth_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_FOURTH_QUESTION))
        self.driver.find_element(*self.LOCATOR_FOURTH_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_FOURTH_ANSWER)

        return self.driver.find_element(*self.LOCATOR_FOURTH_ANSWER).text

    @allure.step('Получение текста ответа на пятый вопрос')
    def get_text_fifth_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_FIFTH_QUESTION))
        self.driver.find_element(*self.LOCATOR_FIFTH_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_FIFTH_ANSWER)

        return self.driver.find_element(*self.LOCATOR_FIFTH_ANSWER).text

    @allure.step('Получение текста ответа на шестой вопрос')
    def get_text_sixth_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_SIXTH_QUESTION))
        self.driver.find_element(*self.LOCATOR_SIXTH_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_SIXTH_ANSWER)

        return self.driver.find_element(*self.LOCATOR_SIXTH_ANSWER).text

    @allure.step('Получение текста ответа на седьмой вопрос')
    def get_text_seventh_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_SEVENTH_QUESTION))
        self.driver.find_element(*self.LOCATOR_SEVENTH_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_SEVENTH_ANSWER)

        return self.driver.find_element(*self.LOCATOR_SEVENTH_ANSWER).text

    @allure.step('Получение текста ответа на восьмой вопрос')
    def get_text_eighth_answer(self):
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_EIGHTH_QUESTION))
        self.driver.find_element(*self.LOCATOR_EIGHTH_QUESTION).click()
        self.wait_for_load_element(self.LOCATOR_EIGHTH_ANSWER)

        return self.driver.find_element(*self.LOCATOR_EIGHTH_ANSWER).text

    @allure.step('Нажатие по кнопке "Яндекс" в шапке страницы')
    def click_on_yandex_button_in_the_header_of_page(self):
        self.driver.find_element(*self.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).click()

    @allure.step('Нажатие по кнопке "Самокат" в шапке страницы')
    def click_on_yandex_button_in_the_header_of_page(self):
        self.driver.find_element(*self.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).click()

    @allure.step('Проверка ссылки в кнопке "Яндекс" в шапке страницы')
    def check_link_in_yandex_button_in_the_header_of_page(self):
        link = self.driver.find_element(*self.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).get_attribute('href')

        if link is None or len(link) == 0 or not ("yandex.ru" in link):
            return None
        else:
            self.driver.find_element(*self.LOCATOR_YANDEX_BUTTON_IN_THE_HEADER).click()
            return True

    @allure.step('Проверка ссылки в кнопке "Яндекс" в шапке страницы')
    def check_link_in_scooter_button_in_the_header_of_page(self):
        link = self.driver.find_element(*self.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).get_attribute('href')

        if link is None or len(link) == 0 or not ("qa-scooter.praktikum-services.ru" in link):
            return None
        else:
            self.driver.find_element(*self.LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER).click()
            return True


class OrderPage:
    driver = None

    def __init__(self, driver):
        self.driver = driver

    LOCATOR_BUTTON_ORDER = [By.CSS_SELECTOR, "div.Header_Nav__AGCXC button.Button_Button__ra12g"]
    LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM = [By.CSS_SELECTOR, "div.Home_FinishButton__1_cWm button.Button_Button__ra12g"]

    LOCATOR_FIELD_NAME = [By.XPATH, ".//div[@class='Order_Form__17u6u'] / .//input[@placeholder='* Имя']"]
    LOCATOR_FIELD_SURNAME = [By.XPATH, ".//div[@class='Order_Form__17u6u'] / .//input[@placeholder='* Фамилия']"]
    LOCATOR_FIELD_ADDRESS = [By.XPATH,
                             ".//div[@class='Order_Form__17u6u'] / .//input[@placeholder='* Адрес: куда привезти заказ']"]
    LOCATOR_FIELD_METRO = [By.XPATH, ".//div[@class='Order_Form__17u6u'] / .//input[@placeholder='* Станция метро']"]
    LOCATOR_BUTTON_WITH_METRO_STATION_NAME = [By.CSS_SELECTOR,
                                              "button[class='Order_SelectOption__82bhS select-search__option']"]
    LOCATOR_FIELD_PHONE = [By.XPATH,
                           ".//div[@class='Order_Form__17u6u'] / .//input[@placeholder='* Телефон: на него позвонит курьер']"]

    LOCATOR_BUTTON_NEXT = [By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    LOCATOR_INACTIVE_FIELD_SELECT_A_DELIVERY_TIME = [By.XPATH,
                                                     ".//div[@class='react-datepicker__input-container']/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    LOCATOR_ACTIVE_FIELD_SELECT_A_DELIVERY_TIME = [By.CSS_SELECTOR,
                                                   "[class='Input_Input__1iN_Z Input_Responsible__1jDKN Input_Filled__1rDxs react-datepicker-ignore-onclickoutside']"]
    LOCATOR_FIELD_RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-arrow"]
    LOCATOR_DROPDOWN_MENU_WITH_RENTAL_PERIOD = [By.CLASS_NAME, "Dropdown-option"]

    LOCATOR_SCOOTER_COLORS_SELECTION = [By.CSS_SELECTOR, "div.Order_Checkboxes__3lWSI label"]
    LOCATOR_FIELD_COMMENT = [By.XPATH,
                             ".//div[@class='Input_InputContainer__3NykH']/input[@class='Input_Input__1iN_Z Input_Responsible__1jDKN']"]
    LOCATOR_ORDER_BUTTON = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp'] / .//button[contains(text(), 'Заказать')]"]
    LOCATOR_BUTTON_YES_IN_FORM_WANT_PLACE_ORDER = [By.XPATH, ".//button[contains(text(), 'Да')]"]

    LOCATOR_MESSAGE_ABOUT_SUCCESSFUL_ORDER_PROCESSING = [By.CSS_SELECTOR, "div.Order_Modal__YZ-d3 div.Order_Text__2broi"]

    @allure.step('Заполнение поля "Имя"')
    def set_field_name(self, name):
        self.driver.find_element(*self.LOCATOR_FIELD_NAME).send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def set_field_surname(self, surname):
        self.driver.find_element(*self.LOCATOR_FIELD_SURNAME).send_keys(surname)

    @allure.step('Заполнение поля "Адресс"')
    def set_field_address(self, address):
        self.driver.find_element(*self.LOCATOR_FIELD_ADDRESS).send_keys(address)

    @allure.step('Заполнение поля "Метро"')
    def set_field_metro(self, metro):
        self.driver.find_element(*self.LOCATOR_FIELD_METRO).send_keys(metro)
        self.driver.find_element(*self.LOCATOR_BUTTON_WITH_METRO_STATION_NAME).click()

    @allure.step('Заполнение поля "Телефон"')
    def set_field_phone(self, phone):
        self.driver.find_element(*self.LOCATOR_FIELD_PHONE).send_keys(phone)

    @allure.step('Нажатие по кнопке "Далее"')
    def click_next_button(self):
        self.driver.find_element(*self.LOCATOR_BUTTON_NEXT).click()

    @allure.step('Нажатие по кнопке "Заказать" в шапке страницы')
    def click_button_order_in_header(self):
        self.driver.find_element(*self.LOCATOR_BUTTON_ORDER).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(self.LOCATOR_BUTTON_NEXT))

    @allure.step('Нажатие по кнопке "Заказать" внизу страницы')
    def click_button_order_at_the_bottom_of_page(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*self.LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM))
        self.driver.find_element(*self.LOCATOR_BUTTON_ORDER_AT_THE_BOTTOM).click()

    @allure.step('Выбор даты доставки')
    def select_date_to_delivery(self, date):
        self.driver.find_element(*self.LOCATOR_INACTIVE_FIELD_SELECT_A_DELIVERY_TIME).send_keys(date)
        self.driver.find_element(*self.LOCATOR_ACTIVE_FIELD_SELECT_A_DELIVERY_TIME).click()

    @allure.step('Заполнение поля "Срок аренды"')
    def select_rental_period(self, day_count):
        self.driver.find_element(*self.LOCATOR_FIELD_RENTAL_PERIOD).click()
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.LOCATOR_DROPDOWN_MENU_WITH_RENTAL_PERIOD))
        self.driver.find_elements(*self.LOCATOR_DROPDOWN_MENU_WITH_RENTAL_PERIOD)[day_count - 1].click()

    @allure.step('Выбор цвета самоката')
    def select_scooter_color(self, color):
        if color == 'black':
            self.driver.find_elements(*self.LOCATOR_SCOOTER_COLORS_SELECTION)[0].click()
        elif color == 'grey':
            self.driver.find_elements(*self.LOCATOR_SCOOTER_COLORS_SELECTION)[1].click()
        elif color == 'grey and black' or color == 'black and grey':
            self.driver.find_elements(*self.LOCATOR_SCOOTER_COLORS_SELECTION)[0].click()
            self.driver.find_elements(*self.LOCATOR_SCOOTER_COLORS_SELECTION)[1].click()

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def set_field_comment(self, comment):
        self.driver.find_element(*self.LOCATOR_FIELD_COMMENT).send_keys(comment)

    @allure.step('Нажатие по кнопке "Заказать" после заполнения всех обязательных полей')
    def click_button_place_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(self.LOCATOR_ORDER_BUTTON))
        self.driver.find_element(*self.LOCATOR_ORDER_BUTTON).click()

    @allure.step('Нажатие по кнопке "Да" в окне "Хотите оформить заказ?"')
    def click_button_yes_in_form_place_order(self):
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(self.LOCATOR_BUTTON_YES_IN_FORM_WANT_PLACE_ORDER))
        self.driver.find_element(*self.LOCATOR_BUTTON_YES_IN_FORM_WANT_PLACE_ORDER).click()

    @allure.step('Получение окна об успешном оформлении заказа')
    def get_successful_create_order_message(self):
        message = self.driver.find_element(*self.LOCATOR_MESSAGE_ABOUT_SUCCESSFUL_ORDER_PROCESSING).text
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
