'''
i want to create a bank account class using python


Here's an example of how you can create a bank account class in Python:
'''
# Define a class named BankAccount
class BankAccount:
    # Dunder init method to initialize the object's attributes
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    # Method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds. Cannot withdraw.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    # Method to get the account balance
    def get_balance(self):
        return f"Account Number: {self.account_number}, Balance: {self.balance}"

# Example usage
account = BankAccount("John Doe","12343", 1000)
account.deposit(500)
print("Account balance: ", account.get_balance())
account.withdraw(200)
print("Account balance: ", account.get_balance())
'''
In this example, we define a `BankAccount` class with methods for depositing and withdrawing money, as well 
as a `get_balance` method to retrieve the current balance of the account. The `__init__` method initializes the 
account with a name, account number and balance. The `deposit` method adds the specified amount to the account 
balance, and the `withdraw` method subtracts the specified amount from the account balance. The `get_balance` method 
simply returns the current balance of the account.

In the example usage, we create an instance of the `BankAccount` class with a name and initial balance of 1000. We 
then deposit and withdraw money from the account, and finally retrieve the current balance using the `get_balance` 
method.
'''