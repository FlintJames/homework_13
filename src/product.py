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
    def create_product(cls, name, description, price, quantity_in_stock):
        product_data = {name, description, price, quantity_in_stock}
        new_product_instance = Product.create_product(product_data)
        return new_product_instance


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = cost