def apply_discount(price, discount):
    '''
    Function that applies a discount to an amount.
    Parameters:
        price: A float value representing the price to apply the discount to.
        discount: The discount percentage to be deducted.
    Returns:
        The final price after applying the discount.
    '''
    return price - price * discount / 100

def apply_IVA(price, percentage):
    '''
    Function that applies a VAT (Value Added Tax) to an amount.
    Parameters:
        price: A float value representing the price to apply the VAT to.
        percentage: The VAT percentage to be added.
    Returns:
        The final price after applying the VAT.
    '''
    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Function that calculates the price of a shopping basket after applying a function to initial prices.
    Parameters:
        basket: A dictionary containing price:discount pairs.
        function: A function that takes two float values and returns another. Typically used for applying discounts or VAT.
    Returns:
        The final price of the shopping basket after applying the function to the initial prices.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total


# Example usage of the code

# Define a dictionary representing the basket with price:discount pairs
basket = {
    100: 10,  # Price: 100, Discount: 10%
    50: 5,    # Price: 50, Discount: 5%
    200: 15   # Price: 200, Discount: 15%
}

# Calculate the total price of the basket after applying discounts
total_price_with_discount = price_basket(basket, apply_discount)
print("Total price with discounts:", total_price_with_discount)

# Calculate the total price of the basket after applying VAT
total_price_with_VAT = price_basket(basket, apply_IVA)
print("Total price with VAT:", total_price_with_VAT)


