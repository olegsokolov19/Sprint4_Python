from pages.main_page import MainPage


class TestClickButtonOnTheHeaderOfThePage:

    def test_link_in_yandex_button_in_the_header_of_page(self, setup):
        main_page = MainPage(setup)
        main_page.go_to_site()

        result = main_page.check_link_in_yandex_button_in_the_header_of_page()

        assert result is not None

    def test_link_in_scooter_button_in_the_header_of_page(self, setup):
        main_page = MainPage(setup)
        main_page.go_to_site()

        result = main_page.check_link_in_scooter_button_in_the_header_of_page()

        assert result is not None
