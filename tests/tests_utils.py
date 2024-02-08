import pytest

from src.utils import Category, Product
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
def product_orange():
    return Product('Orange', 'Fresh orange', 79.99, 5)
def test_init(product_orange):
    assert product_orange.name == 'Orange'
    assert product_orange.description == 'Fresh orange'
    assert product_orange.price == 79.99
    assert product_orange.quantity_in_stock == 5