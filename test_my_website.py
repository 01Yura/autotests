from selenium import webdriver # для взаимодействия с браузером
from selenium.webdriver.common.by import By # для поиска элементов на веб-странице
from selenium.webdriver.firefox.options import Options # для запуска в режиме headless
import pytest
import time # для ожидания

@pytest.fixture
def driver(): # обычно пишут не driver, а driver
    options = Options()
    options.add_argument('--headless')
    driver=webdriver.Firefox(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5) # включить неявное ожидание, иначе тест загнется, так как прога отрабатывает слишком быстро и сайт не успевает загузится
    yield driver
    driver.close()

def test_check_ip_link(driver):
    driver.get('https://yura.it-website.online')
    check_ip_link = driver.find_element(By.LINK_TEXT, "Check IP")
    check_ip_link.click()
    time.sleep(2)
    count = driver.find_elements(By.CSS_SELECTOR, value='h1')
    assert len(count) == 3

def test_check_hostname_link(driver):
    driver.get('https://yura.it-website.online')
    check_hostname_link = driver.find_element(By.LINK_TEXT, "Check Hostname")
    check_hostname_link.click()
    time.sleep(2)  # Подождем немного для загрузки страницы
    count = driver.find_elements(By.CSS_SELECTOR, value='h1')
    assert len(count) == 1
