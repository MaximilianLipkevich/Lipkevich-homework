class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0

    def add(self, product, amount):
        if product.name not in self.products:
            self.products[product.name] = {
                'product': product,
                'amount': amount,
                'price': product.price * 1.3
            }
        else:
            self.products[product.name]['amount'] += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product in self.products.values():
            if identifier_type == 'name' and product['product'].name == identifier:
                product['price'] *= 1 - percent / 100
            elif identifier_type == 'type' and product['product'].type == identifier:
                product['price'] *= 1 - percent / 100

    def sell_product(self, product_name, amount):
        if product_name in self.products and self.products[product_name]['amount'] >= amount:
            self.products[product_name]['amount'] -= amount
            self.income += self.products[product_name]['price'] * amount
        else:
            raise ValueError(f'Not enough {product_name} in stock')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [f'{product["product"].name}: {product["amount"]}' for product in self.products.values()]

    def get_product_info(self, product_name):
        if product_name in self.products:
            return (product_name, self.products[product_name]['amount'])
        else:
            raise ValueError(f'{product_name} not found in the store')

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
