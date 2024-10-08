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

def test_open_galaxy_s6(driver):
    driver.get('https://demoblaze.com/index.html')
    galaxy_s6 = driver.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]') # ищем элемент и сохраняем в переменную
    galaxy_s6.click()
    title = driver.find_element(By.CSS_SELECTOR, value='h2')
    assert title.text == 'Samsung galaxy s6'

def test_two_monitors(driver):
    driver.get('https://demoblaze.com/index.html')
    monitor_link=driver.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(3)
    monitors = driver.find_elements(By.CSS_SELECTOR, value='.card')
    assert len(monitors) == 2