from src.product import Product, all_products


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
        Category.number_of_unique_products += len(products)

    def add_product(self, product):
        Category.number_of_unique_products += 1
        return self.__products.append(product)

    @property
    def products(self):
        list_of_products = []
        for product in self.__products:
            name = product.name
            price = product.price
            quantity = product.quantity
            list_of_products.append(f"{name}, {price} руб. Остаток: {quantity} шт.")
        return list_of_products



    def __len__(self):
        all_quantity = 0
        for quantity in self.__products:
            quantity = quantity.quantity
            all_quantity = all_quantity + quantity
        return len(self.all_quantity)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.all_quantity)} шт."


category_1 = Category('Фрукты', 'Свежие фрукты', all_products)

print(category_1.products[0])
print(category_1.products[1])
print(category_1.products[2])

print(category_1)
