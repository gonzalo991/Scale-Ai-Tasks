class DebitCard:
    # Define the dunder init method
    def __init__(self, card_number, card_expiration_date, card_name, card_cvv, card_balance):
        self._card_number = card_number
        self._card_expiration_date = card_expiration_date
        self._card_name = card_name
        self._card_cvv = card_cvv
        self._card_balance = card_balance
        
    # Define the dunder str
    def __str__(self):
        return f"[ Debit Card Number: {self._card_number}, Expiration Date: {self._card_expiration_date}, Name: {self._card_name}, CVV: {self._card_cvv}, Balance: {self._card_balance}] "

    # Define getter for attributes that will not change
    @property
    def card_number(self):
        return self._card_number
    
    @property
    def card_expiration(self):
        return self._card_expiration_date
    
    @property
    def card_cvv(self):
        return self._card_cvv
    
    # Define getters and setters for balance
    @property
    def card_balance(self):
        return self._card_balance
    
    @card_balance.setter
    def card_balance(self, new_balance):
        self._card_balance = new_balance