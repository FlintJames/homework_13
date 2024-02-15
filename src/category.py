


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

    def add_product(self, products):
        Category.number_of_unique_products += 1
        return self.__products.append(products)


    @property
    def products(self):
        list_of_products = []
        for products in self.__products:
            list_of_products.append(f"{products['name']}, {products['price']} руб. Остаток: {products['quantity']} шт.")
        return list_of_products



category_1 = Category('Фрукты', 'Свежие фрукты', [
                                                 {'name': 'Яблоко',
                                                  'price': 70,
                                                  'quantity': 15
                                                  },
                                                 {'name': 'Апельсин',
                                                  'price': 90,
                                                  'quantity': 7
                                                  },
                                                 {'name': 'Банан',
                                                  'price': 150,
                                                  'quantity': 25
                                                  }
                                                 ])


category_2 = Category('Овощи', 'Свежие овощи', [
                                                 {'name': 'Огурец',
                                                  'price': 300,
                                                  'quantity': 10
                                                  },
                                                 {'name': 'Томат',
                                                  'price': 200,
                                                  'quantity': 25
                                                  },
                                                 {'name': 'Картофель',
                                                  'price': 20,
                                                  'quantity': 15
                                                  }
                                                 ])
print(category_1.products)

