class Wallet:
    def __init__(self,name, money, credit_cards, debit_cards):
        self.name = name
        self.money = money
        self.credit_cards = credit_cards
        self.debit_cards = debit_cards

    def add_money(self, amount):
        self.money += amount

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return f"Wallet: {self.name}, Balance: {self.money}"