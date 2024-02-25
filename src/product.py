
class Product:
    name: str
    description: str
    price: float
    quantity: int
    colour: str


    def __init__(self, name, description, price, quantity, color):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.colour = color


    @classmethod
    def create_product(cls, product_data):
        name = product_data['name']
        description = product_data['description']
        price = product_data['price']
        quantity = product_data['quantity']
        color = product_data['color']
        return cls(name, description, price, quantity, color)


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = cost

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return (self.__price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError



class Smartphone(Product):
    efficiency: float
    model: str
    amount_of_internal_memory: float

    def __init__(self, efficiency, model, amount_of_internal_memory):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.amount_of_internal_memory = amount_of_internal_memory

class Lawn_grass(Product):
    country_of_origin: str
    germination_period: int


    def __init__(self, country_of_origin, germination_period):
        super().__init__(name, description, price, quantity, color)
        self.country_of_origin = country_of_origin
        self.germination_period = germination_period


pear_data = {
    'name': 'Груша',
    'description': 'Спелая ароматная груша',
    'price': 99.99,
    'quantity': 30,
    'color': 'Зелёная'
}
apple_data = {
    'name': 'Яблоко',
    'description': 'Красное сочное яблоко',
    'price': 66.70,
    'quantity': 22,
    'color': 'Красное'
}
new_product = Product.create_product(pear_data)
print(new_product.name)

product_1 = Product('Яблоко', 'Сочное яблоко', 79.90, 15, 'Красное')
product_2 = Product('Апельсин', 'Красный ароматный апельсин', 69.99, 30, 'Оранжевый')
product_3 = Product('Банан', 'Жёлтый манящий банан', 69.99, 30, 'Жёлтый')
all_products = [product_1, product_2, product_3]

print(product_1)

print(product_1 + product_2)