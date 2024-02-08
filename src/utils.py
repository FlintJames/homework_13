


class Category:
    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1
        Category.number_of_unique_products == len(products)

category_1 = Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])
category_2 = Category('Vegetables', 'Fresh vegetables', ['cucumber', 'tomato', 'potato'])

class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int


    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock