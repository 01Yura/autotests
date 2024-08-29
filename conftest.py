from selenium import webdriver # для взаимодействия с браузером
import pytest

@pytest.fixture
def browser(): # обычно пишут не browser, а driver
    browser=webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(5) # включить неявное ожидание, иначе тест загнется, так как прога отрабатывает слишком быстро и сайт не успевает загузится
    yield browser
    browser.close()