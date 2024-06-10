import unittest
from python_e_pood import Shop, Customer, Item, Basket

class TestShopping(unittest.TestCase):
    def setUp(self):
        self.item1 = Item('Apple', 10, 5)
        self.item2 = Item('Banana', 20, 0)
        self.customer = Customer(1, 'Regular Customer', 100)
        self.shop = Shop()

    def test_add_item(self):
        self.customer.basket.add_item(self.item1)
        self.assertEqual(len(self.customer.basket.items), 1)

    def test_add_item_out_of_stock(self):
        with self.assertRaises(Exception):
            self.customer.basket.add_item(self.item2)

    def test_remove_item(self):
        self.customer.basket.add_item(self.item1)
        self.customer.basket.remove_item(self.item1)
        self.assertEqual(len(self.customer.basket.items), 0)

    def test_remove_item_not_in_basket(self):
        with self.assertRaises(Exception):
            self.customer.basket.remove_item(self.item1)

    def test_purchase(self):
        self.customer.basket.add_item(self.item1)
        self.customer.purchase(self.shop)
        self.assertEqual(self.customer.balance, 90)
        self.assertEqual(len(self.customer.history), 1)

    def test_purchase_exceeds_balance(self):
        self.customer.basket.add_item(self.item1)
        self.customer.balance = 5
        with self.assertRaises(Exception):
            self.customer.purchase(self.shop)

    def test_golden_customer_discount(self):
        golden_customer = Customer(2, 'Golden Customer', 100)
        golden_customer.basket.add_item(self.item1)
        golden_customer.purchase(self.shop)
        self.assertEqual(golden_customer.balance, 91)

    def test_purchase_empty_basket(self):
        with self.assertRaises(Exception):
            self.customer.purchase(self.shop)

    def test_purchase_insufficient_balance(self):
        self.customer.basket.add_item(self.item1)
        self.customer.balance = 5
        with self.assertRaises(Exception):
            self.customer.purchase(self.shop)

if __name__ == '__main__':
    unittest.main()
