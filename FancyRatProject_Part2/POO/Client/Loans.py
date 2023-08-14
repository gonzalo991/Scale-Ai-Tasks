class Loans:
    # Define the dunder init method
    def __init__(self, loan_type, loan_amount, loan_rate, loan_term, loan_repayment):
        self._loan_type = loan_type
        self._loan_amount = loan_amount
        self._loan_rate = loan_rate
        self._loan_term = loan_term
        self._loan_repayment = loan_repayment
        
    # Define the dunder str
    def __str__(self):
        return f"[ Loan Type: {self._loan_type}, Amount: {self._loan_amount}, Rate: {self._loan_rate}, Term: {self._loan_term}, Repayment: {self._loan_repayment}] "

    # Define getters and setters
    @property
    def loan_type(self):
        return self._loan_type
    
    @loan_type.setter
    def loan_type(self, new_loan_type):
        self.loan_type = new_loan_type
    
    @property
    def loan_amount(self):
        return self._loan_amount
    
    @loan_amount.setter
    def loan_amount(self, new_amount):
        self._loan_amount = new_amount
    
    @property
    def loan_rate(self):
        return self._loan_rate
    
    @loan_rate.setter
    def loan_rate(self, new_rate):
        self._loan_rate = new_rate
    
    @property
    def loan_term(self):
        return self._loan_term
    
    @loan_term.setter
    def loan_term(self, new_term):
        self._loan_term = new_term
    
    @property
    def loan_repayment(self):
        return self._loan_repayment
    
    @loan_repayment.setter
    def loan_repayment(self, new_repayment):
        self._loan_repayment = new_repayment