
class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int


    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def create_product(cls, product_data):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        return cls(name, description, price, quantity)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = cost


pear_data = {
    'name': 'Груша',
    'description': 'Спелая ароматная груша',
    'price': 99.99,
    'quantity': 30
}
apple_data = {
    'name': 'Яблоко',
    'description': 'Красное сочное яблоко',
    'price': 66.70,
    'quantity': 22
}
new_product = Product.create_product(pear_data)
print(new_product.name)

product_1 = Product('Яблоко', 'Сочное яблоко', 79.90, 15)
product_2 = Product('Апельсин', 'Красный ароматный апельсин', 69.99, 30)
product_3 = Product('Банан', 'Жёлтый манящий банан', 69.99, 30)
all_products = [product_1, product_2, product_3]