import random

from pages.order_page import OrderPage


class TestCreateOrder:

    name = 'Иван'
    surname = 'Сидоров'
    address = 'Лубянка, 2'
    metro = random.choice(['Лубянка', 'Сокольники', 'Тверская', 'Орехово', 'Спартак'])
    phone = '89129999999'
    date = '05.10.2022'
    rental = 1
    color = 'black'

    def test_create_order_button_at_the_top_page(self, setup):
        order_page = OrderPage(setup)
        order_page.go_to_site()
        order_page.click_button_order_in_header()

        order_page.fill_all_required_fields(self.name, self.surname, self.address, self.metro, self.phone,
                                            self.date, self.rental, self.color)
        order_page.click_button_place_order()
        order_page.click_button_yes_in_form_place_order()

        order_number = order_page.get_successful_create_order_message()
        assert order_number is not None

    def test_create_order_button_at_the_buttom_page(self, setup):
        order_page = OrderPage(setup)
        order_page.go_to_site()
        order_page.go_to_main_page()

        order_page.click_button_order_at_the_bottom_of_page()

        order_page.fill_all_required_fields(self.name, self.surname, self.address, self.metro, self.phone,
                                            self.date, self.rental, self.color, comment='Не звоните')
        order_page.click_button_place_order()
        order_page.click_button_yes_in_form_place_order()

        order_number = order_page.get_successful_create_order_message()
        assert order_number is not None
