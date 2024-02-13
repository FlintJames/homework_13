import pytest

from src.product import Product

@pytest.fixture
def product_orange():
    return Product('Orange', 'Fresh orange', 79.99, 5)
def test_init(product_orange):
    assert product_orange.name == 'Orange'
    assert product_orange.description == 'Fresh orange'
    assert product_orange.price == 79.99
    assert product_orange.quantity_in_stock == 5

def test_getter_product_orange(product_orange):
    assert product_orange.price == 79.99

def test_setter_product_orange_less_zero(product_orange):
    product_orange.price = -50
    assert product_orange.price == 79.99


def test_setter_product_orange_normal(product_orange):
    product_orange.price = 129.99
    assert product_orange.price == 129.99