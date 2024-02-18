import pytest

from src.category import Category

@pytest.fixture
def category_fruits():
    return Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])
def test_init(category_fruits):
    assert category_fruits.name == 'Fruits'
    assert category_fruits.description == 'Fresh fruits'
    assert category_fruits.products == ['apple', 'orange', 'banana']

@pytest.fixture
def number_of_categories():
    return Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'],
                    'Vegetables', 'Fresh vegetables', ['cucumber', 'tomato', 'potato'])

def test_init(number_of_categories):
    assert Category.number_of_categories == 2

@pytest.fixture
def number_of_unique_products():
    return Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])
def test_init(number_of_unique_products):
    assert Category.number_of_unique_products == 6

def test___len__():
    assert 3

