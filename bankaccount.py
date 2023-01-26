import unittest

class BankAccount:
    """A simple bank account class"""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def deposit(self, amount):
        """Deposit money into the account"""
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        """Check the current balance of the account"""
        return self.balance
    
class BankAccountTest(unittest.TestCase):
    """Unit tests for the BankAccount class"""
    
    def setUp(self):
        self.account = BankAccount("John Doe", 100)
        
    def test_deposit(self):
        self.assertEqual(self.account.deposit(50), 150)
        
    def test_withdraw(self):
        self.assertEqual(self.account.withdraw(50), 50)
        
    def test_withdraw_insufficient_funds(self):
        self.assertEqual(self.account.withdraw(150), "Insufficient funds")
        
    def test_check_balance(self):
        self.assertEqual(self.account.check_balance(), 100)
        
if __name__ == "__main__":
    unittest.main()
