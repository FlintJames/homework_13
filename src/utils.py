


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
        Category.number_of_unique_products += 1

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