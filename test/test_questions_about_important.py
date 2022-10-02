from selenium import webdriver

from PageObjects import MainPage


class TestQuestionAboutImportant:

    driver = None
    url = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.url = 'https://qa-scooter.praktikum-services.ru/'

    def test_open_first_faq_element(self):
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_first_answer()

        assert elem == expected_text

    def test_open_second_faq_element(self):
        expected_text = 'Пока что у нас так: один заказ — один самокат. ' \
                        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_second_answer()

        assert elem == expected_text

    def test_open_third_faq_element(self):
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. ' \
                        'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. ' \
                        'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_third_answer()

        assert elem == expected_text

    def test_open_fourth_faq_element(self):
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_fourth_answer()

        assert elem == expected_text

    def test_open_fifth_faq_element(self):
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_fifth_answer()

        assert elem == expected_text

    def test_open_sixth_faq_element(self):
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если ' \
                        'будете кататься без передышек и во сне. Зарядка не понадобится.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_sixth_answer()

        assert elem == expected_text

    def test_open_seventh_faq_element(self):
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_seventh_answer()

        assert elem == expected_text

    def test_open_eighth_faq_element(self):
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

        main_page = MainPage(self.driver)
        self.driver.get(self.url)
        main_page.scroll_into_view_FAQ_elements()

        elem = main_page.get_text_eighth_answer()

        assert elem == expected_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
