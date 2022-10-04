import pytest
from selenium import webdriver


@pytest.fixture()
def setup():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()
