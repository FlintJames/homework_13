from src.category import Category

class Product:
    name: str
    description: str
    price: float
    quantity_in_stock: int


    def __init__(self, name, description, price, quantity_in_stock):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_in_stock = quantity_in_stock


    @classmethod
    def create_product(cls, product_data):
        name, description, price, quantity_in_stock = product_data
        new_product_instance = Product.create_product(product_data)
        return cls(name, description, price, quantity_in_stock)


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
    'quantity_in_stock': 30
}
apple_data = {
    'name': 'Яблоко',
    'description': 'Красное сочное яблоко',
    'price': 66.70,
    'quantity_in_stock': 22
}

# создаем экземпляры, отдавая в метод данные
pear = Category.create_product(pear_data)
apple = Category.create_product(apple_data)

print(pear.name)

print(apple.name)

