import unittest
from python_e_pood import Shop, Customer, Item, Basket

class TestShop(unittest.TestCase):
    def setUp(self):
        self.shop = Shop()
        self.customer = Customer(1, "Regular", 100)
        self.item = Item("Apple", 10, 5)
        self.basket = Basket()

    def test_add_product(self):
        self.shop.add_product(self.item)
        self.assertIn(self.item, self.shop.products)

    def test_add_customer(self):
        self.shop.add_customer(self.customer)
        self.assertIn(self.customer, self.shop.customers)

    def test_add_purchase(self):
        self.basket.add_item(self.item)
        self.customer.basket.append(self.basket)
        self.customer.purchase(self.basket)
        self.shop.add_purchase(self.basket)
        self.assertIn(self.basket, self.shop.purchases)

    def test_customer_purchase(self):
        self.basket.add_item(self.item)
        self.customer.basket.append(self.basket)
        self.customer.purchase(self.basket)
        self.assertEqual(self.customer.balance, 90)
        self.assertEqual(self.customer.history, [self.basket])

    def test_basket_cost(self):
        self.basket.add_item(self.item)
        self.assertEqual(self.basket.cost("Regular"), 10)
        self.assertEqual(self.basket.cost("Golden Customer"), 9)

if __name__ == "__main__":
    unittest.main()