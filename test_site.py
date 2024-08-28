from selenium import webdriver # для взаимодействия с браузером
from selenium.webdriver.common.by import By # для поиска элементов на веб-странице
import pytest
import time # для ожидания

@pytest.fixture
def browser(): # обычно пишут не browser, а driver
    browser=webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(5) # включить неявное ожидание, иначе тест загнется, так как прога отрабатывает слишком быстро и сайт не успевает загузится
    yield browser
    browser.close()

def test_open_galaxy_s6(browser):
    browser.get('https://demoblaze.com/index.html')
    galaxy_s6 = browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]') # ищем элемент и сохраняем в переменную
    galaxy_s6.click()
    title = browser.find_element(By.CSS_SELECTOR, value='h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(browser):
    browser.get('https://demoblaze.com/index.html')
    monitor_link=browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(3)
    monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    assert len(monitors) == 2