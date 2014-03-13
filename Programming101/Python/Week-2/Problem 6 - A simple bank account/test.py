# DOCUMENTATION

# IMPORTS
import bank
import unittest


# main
class BankAccountTest(unittest.TestCase):
    def setUp(self):
        self.bank_account = bank.BankAccount()

    def test_initial_balance(self):
        bank.__balance = 0
        self.assertEqual(0, self.bank_account.get_balance())

    def test_deposit_amount(self):
        result = self.bank_account.deposit_money(100)
        self.assertTrue(result)

        self.assertEqual(100, self.bank_account.get_balance())

    def test_deposit_negative_amount(self):
        result = self.bank_account.deposit_money(-100)
        self.assertFalse(result)

        self.assertEqual(0, self.bank_account.get_balance())

    def test_withdraw_amount(self):
        self.bank_account.deposit_money(600)

        result = self.bank_account.withdraw_money(500)
        self.assertTrue(result)

    def test_withdraw_amount_exceeding_balance(self):
        result = self.bank_account.withdraw_money(100)
        self.assertFalse(result)

        self.assertEqual(0, self.bank_account.get_balance())


# PROGRAM RUN
if __name__ == '__main__':
    unittest.main()
