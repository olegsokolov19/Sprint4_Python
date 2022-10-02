from selenium import webdriver
import random

from PageObjects import OrderPage


class TestCreateOrder:
    driver = None
    url = None

    name = 'Иван'
    surname = 'Сидоров'
    address = 'Лубянка, 2'
    metro = random.choice(['Лубянка', 'Сокольники', 'Тверская', 'Орехово', 'Спартак'])
    phone = '89129999999'
    date = '05.10.2022'
    rental = 1
    color = 'black'

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.url = 'https://qa-scooter.praktikum-services.ru/'

    def test_create_order_button_at_the_top_page(self):
        order_page = OrderPage(self.driver)
        self.driver.get(self.url)
        order_page.click_button_order_in_header()

        order_page.fill_all_required_fields(self.name, self.surname, self.address, self.metro, self.phone,
                                            self.date, self.rental, self.color)
        order_page.click_button_place_order()
        order_page.click_button_yes_in_form_place_order()

        order_number = order_page.get_successful_create_order_message()
        assert order_number is not None

    def test_create_order_button_at_the_buttom_page(self):
        order_page = OrderPage(self.driver)
        self.driver.get(self.url)
        order_page.click_button_order_at_the_bottom_of_page()

        order_page.fill_all_required_fields(self.name, self.surname, self.address, self.metro, self.phone,
                                            self.date, self.rental, self.color, comment='Не звоните')
        order_page.click_button_place_order()
        order_page.click_button_yes_in_form_place_order()

        order_number = order_page.get_successful_create_order_message()
        assert order_number is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
