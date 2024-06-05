def main():
    class Customer:
        def __init__(self, customer_id, customer_type, balance):
            self.customer_id = customer_id
            self.basket = []
            self.customer_type = customer_type
            self.history = []
            self.balance = balance

        def check_history(self):
            return self.history[::-1]

        def purchase(self, basket):
            if not self.basket:
                raise Exception("Ostukorv on tühi.")
            elif self.balance < basket.cost():
                raise Exception("Arvel pole piisavalt raha ostu sooritamiseks.")
            else:
                for item in self.basket:
                    if item.amount <= 0:
                        raise Exception("Ostukorvis on toode, mis on hetkel otsas. Ost jäi sooritamata.")
                self.balance -= basket.cost()
                self.history.append(basket)
                self.basket = []

    class Item:
        def __init__(self, name, price, amount):
            self.name = name
            self.price = price
            self.amount = amount

    class Basket:
        def __init__(self):
            self.items = []

        def add_item(self, item):
            if item.amount <= 0:
                raise Exception("Toode on hetkel otsas.")
            else:
                self.items.append(item)
                item.amount -= 1

        def remove_item(self, item):
            if not self.items:
                raise Exception("Ostukorv on juba tühi.")
            else:
                self.items.remove(item)
                item.amount += 1

        def cost(self, customer_type):
            if customer_type == "Golden Customer":
                return sum([item.price * 0.9 for item in self.items])
            else:
                return sum([item.price for item in self.items])

    class Shop:
        def __init__(self):
            self.products = []
            self.purchases = []
            self.customers =[]

        def add_product(self, product):
            if product in self.products:
                raise Exception("Toode on juba poes.")
            else:
                self.products.append(product)

        def add_customer(self, customer):
            self.customers.append(customer)

        def add_purchase(self, purchase):
            self.purchases.append(purchase)

if __name__ == "__main__":
    main()