import CreditCard
import DebitCard
import Loans
import Client

creditCard = CreditCard("4895-4242-4", "2023-08-15", "John Dow", "123", "$1000")
debitCard = DebitCard("4895-4242-43", "2025-03-23", "John Dow", "134", "$600")
loans = Loans("personal","$2000","5.99", "2 years", "$100/month")
# Example usage
client = Client("John Doe","Smith","1245664", creditCard, debitCard, loans)

print(client)