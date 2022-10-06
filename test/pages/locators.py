from selenium.webdriver.common.by import By


class MainPageLocators:
    driver = None

    LOCATOR_ACCORDION_ELEMENTS = [By.CSS_SELECTOR, "div.accordion__item"]

    LOCATOR_BUTTON_COOKIE = [By.CLASS_NAME, "App_CookieButton__3cvqF"]

    LOCATOR_YANDEX_BUTTON_IN_THE_HEADER = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    LOCATOR_SCOOTER_BUTTON_IN_THE_HEADER = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]

    LOCATOR_HOME_HEADER = [By.CLASS_NAME, "Home_Header__iJKdX"]


class OrderPageLocators:
    driver = None

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
