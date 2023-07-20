import random

def is_prime(n):
    """
    Simple function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def LV(n):
    """
    Las Vegas algorithm implementation for finding a prime number with n digits.
    """
    start = 10**(n-1)
    end = 10**n - 1
    while True:
        number = random.randint(start, end)
        if is_prime(number):
            return number

# Use the LV function to find a 5-digit prime number
prime = LV(5)
print(prime)
