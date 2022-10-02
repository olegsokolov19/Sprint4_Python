from selenium import webdriver
from PageObjects import MainPage


class TestClickButtonOnTheHeaderOfThePage:

    driver = None
    url = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.url = 'https://qa-scooter.praktikum-services.ru/'

    def test_link_in_yandex_button_in_the_header_of_page(self):
        main_page = MainPage(self.driver)
        self.driver.get(self.url)

        result = main_page.check_link_in_yandex_button_in_the_header_of_page()

        assert result is not None

    def test_link_in_scooter_button_in_the_header_of_page(self):
        main_page = MainPage(self.driver)
        self.driver.get(self.url)

        result = main_page.check_link_in_scooter_button_in_the_header_of_page()

        assert result is not None

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
