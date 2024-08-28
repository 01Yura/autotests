# сам файл должен начинаться с test_
# запускается из терминала командой pytest -v
import pytest

@pytest.fixture
def before_after():
    print ('\nBefore test')
    yield
    print('\nAfter test')

def test_1(): # название функции должно начмнаться с test_
    assert 1==1

def test_2(before_after): # выполняем весь тест командой "pytest -v -s"
    assert 2==2 