'''
now i want to create a person class who has a bank account

Here's an example of how you can create a Person class with a bank account getting as parameter the class BankAccount 
created above:
'''
from Bank_Account import BankAccount
from Wallet import Wallet

class Person:
    def __init__(self, dni_number, name, surname, bank_account, address, wallet):
        self.dni_number = dni_number
        self.name = name
        self.surname = surname
        self.bank_account = bank_account
        self.address = address
        self.wallet = wallet

    def buy_something(self, amount):
        self.bank_account.withdraw(amount)
        return self.bank_account.get_balance()

    def save_money(self, amount):
        self.bank_account.deposit(amount)
        return self.bank_account.get_balance()

    def account_balance(self):
        return self.bank_account.get_balance()
    
    def get_my_address(self):
        return self.address.get_address()
    
    def spend_amount(self, amount):
        self.wallet.spend_money(amount)
        return self.wallet.get_balance()
    
    def add_amount(self, amount):
        self.wallet.add_money(amount)
        return self.wallet.get_balance()
    
    def get_my_wallet(self):
        return self.wallet.get_balance()

# Example usage
person = Person("745647","John", "Doe", BankAccount("John Doe", "12343", 1000))
person.save_money(500)
print("Account 12343 balance: ", person.account_balance())
person.buy_something(200)
print("Account 12343 balance: ", person.account_balance())
'''
In this example, we define a `Person` class with a `bank_account` attribute that is an instance of the 
`BankAccount` class. The `Person` class has methods for save money and buy_something that use mothods from 
the bank account, as well as a `get_balance` withdraw and deposit_monety methods.

In the example usage, we create an instance of the `Person` class with a name and an initial balance of 
1000 in their bank account. We then save money and buy something using the account, and finally retrieve 
the current balance using the `account_balance` method.
'''