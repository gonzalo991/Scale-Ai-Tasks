# Define original classes for different payment methods

class PayPal:
    def __init__(self, amount, service):
        self.amount = amount
        self.service = service
    
    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount} for {self.service}")

class EasyPayment:
    def __init__(self, amount, service):
        self.amount = amount
        self.service = service
    
    def make_payment(self):
        print(f"Making EasyPayment payment of ${self.amount} for {self.service}")

class FastPayment:
    def __init__(self, amount, service):
        self.amount = amount
        self.service = service

    def make_payment(self):
        print(f'Making FastPayment payment of ${self.amount} for {self.service}')

# Define a common interface for payment gateways

class PaymentGateway:
    def process_payment(self):
        pass

# Define adapters for different payment methods

class PayPalAdapter(PaymentGateway):
    def __init__(self, paypal_payment):
        self.paypal_payment = paypal_payment
    
    def process_payment(self):
        self.paypal_payment.process_payment()

class EasyPaymentAdapter(PaymentGateway):
    def __init__(self, easy_payment):
        self.easy_payment = easy_payment
    
    def process_payment(self):
        self.easy_payment.make_payment()

class FastPaymentAdapter(PaymentGateway):
    def __init__(self, fast_payment):
        self.fast_payment = fast_payment
    
    def process_payment(self):
        self.fast_payment.make_payment()

# Define a factory class to create payment gateway adapters

class PaymentGatewayFactory:
    adapter_types = {
        'PayPal': PayPalAdapter,
        'EasyPayment': EasyPaymentAdapter,
        'FastPayment': FastPaymentAdapter
    }

    @staticmethod
    def create_payment_gateway(payment_type, original_payment):
        if payment_type in PaymentGatewayFactory.adapter_types:
            adapter_class = PaymentGatewayFactory.adapter_types[payment_type]
            return adapter_class(original_payment)
        else:
            raise ValueError(f"Invalid payment type: {payment_type}")

    @staticmethod
    def calculate_total_payments(payment_adapters):
        total = 0
        for payment_adapter in payment_adapters:
            try:
                total += payment_adapter.paypal_payment.amount
            except AttributeError:
                pass
            try:
                total += payment_adapter.easy_payment.amount
            except AttributeError:
                pass
            try:
                total += payment_adapter.fast_payment.amount
            except AttributeError:
                pass
        return total

# Define a function to process payments using a payment gateway

def make_payment(payment_gateway):
    try:
        payment_gateway.process_payment()
    except Exception as e:
        print(f"Payment processing error: {str(e)}")

# Create instances of different payment methods

paypal_payment = PayPal(100, "Water Service")
easy_payment = EasyPayment(150, "Light Service")
fast_payment = FastPayment(200, "Gas Service")

# Create adapters using the factory for different payment types

try:
    paypal_adapter = PaymentGatewayFactory.create_payment_gateway('PayPal', paypal_payment)
    easy_adapter = PaymentGatewayFactory.create_payment_gateway('EasyPayment', easy_payment)
    fast_adapter = PaymentGatewayFactory.create_payment_gateway('FastPayment', fast_payment)
except ValueError as ve:
    print(ve)

# Process payments using the common interface

make_payment(paypal_adapter)
make_payment(easy_adapter)
make_payment(fast_adapter)

# Calculate total payments

payment_adapters = [paypal_adapter, easy_adapter, fast_adapter]
total_payments = PaymentGatewayFactory.calculate_total_payments(payment_adapters)
print(f"Total payments: ${total_payments}")
