


class Category:
    name: str
    description: str
    products: list

    number_of_categories = 0
    number_of_unique_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.number_of_categories += 1
        Category.number_of_unique_products == len(products)

    def get_products(self, products):
        return self.__products.append(products)


    @property
    def products(self):
        self.__products = input()
        return f'{self.__products}, руб. Остаток: шт.'




category_1 = Category('Fruits', 'Fresh fruits', ['apple', 'orange', 'banana'])
category_2 = Category('Vegetables', 'Fresh vegetables', ['cucumber', 'tomato', 'potato'])
print(category_1.products)

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


    @classmethod
    def add_product(cls, name, description, price, quantity_in_stock):
        new_product = {
            'name': name,
            'description': description,
            'price': price,
            'quantity_in_stock': quantity_in_stock
        }
        return new_product


    @property
    def price(self):
        return self.price

    @price.setter
    def price(self):
        if self.price <= 0:
            print("Введена некорректная цена")
            self.price = None