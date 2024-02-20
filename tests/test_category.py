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
    return Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])

def test___init__(number_of_categories):
    assert Category.number_of_categories == 1

@pytest.fixture
def number_of_unique_products():
    return Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])
def test_init(number_of_unique_products):
    assert Category.number_of_unique_products == 6

@pytest.fixture
def product_orange():
    return Product('Fruits', 'Fresh orange', 79.99, 5)

def test___str__(product_orange):
    assert f"Fruits, количество продуктов: 5 шт."

