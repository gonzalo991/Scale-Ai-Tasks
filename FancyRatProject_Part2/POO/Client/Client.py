class Client:
    # Define the dunder init method
    def __init__(self, name, surname, dni_number, credit_card, debit_card, loans):
        self._name = name
        self._surname = surname
        self._dni_number = dni_number
        self._credit_card = credit_card
        self._debit_card = debit_card
        self._loans = loans
        
    def __str__(self):
        return f"[ Name: {self._name} {self._surname}, DNI: {self._dni_number}, [Credit Card Info: {self._credit_card}], [Debit Card Info: {self._debit_card}], [Loans Info: {self._loans}] ]"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,new_name):
        self._name = new_name

    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, new_surname):
        self._surname = new_surname

    @property
    def dni_number(self):
        return self._dni_number
    
    @dni_number.setter
    def dni_number(self, new_dni):
        self._dni_number