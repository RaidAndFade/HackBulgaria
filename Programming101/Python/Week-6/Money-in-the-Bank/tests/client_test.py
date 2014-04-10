import sys
import unittest
sys.path.append("..")

from Client import Client


class ClientTests(unittest.TestCase):

    def setUp(self):
        self.test_client = Client(1, "Ivo", 200000.00, "Bitcoin mining makes me rich")

    def test_client_id(self):
        self.assertEqual(self.test_client.get_id(), 1)

    def test_client_name(self):
        self.assertEqual(self.test_client.get_username(), "Ivo")

    def test_client_balance(self):
        self.assertEqual(self.test_client.get_balance(), 200000.00)

    def test_client_message(self):
        self.assertEqual(self.test_client.get_message(), "Bitcoin mining makes me rich")

    def test_deposit(self):
        self.test_client.deposit(500)
        self.assertEqual(200500.00, self.test_client.get_balance())

    def test_withdraw(self):
        self.test_client.withdraw(200000)
        self.assertEqual(0, self.test_client.get_balance())

    def test_withdraw_more_than_available(self):
        self.test_client.withdraw(210000)
        self.assertEqual(0, self.test_client.get_balance())


if __name__ == '__main__':
    unittest.main()
