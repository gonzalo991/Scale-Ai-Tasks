'''
# Define the list of seven natural numbers
numbers = [1, 2, 3, 4, 5, 6, 7]

# Initialize variables to store the product of odd numbers and the count of even numbers
product_of_odd_numbers = 1
even_count = 0

# Iterate through the numbers
for num in numbers:
    if num % 2 == 1:  # Check if the number is odd
        product_of_odd_numbers *= num  # Multiply odd numbers together
    else:
        even_count += 1  # Increment the count of even numbers

# Print the product of odd numbers and the count of even numbers
print(f"The product of odd numbers is {product_of_odd_numbers}")
print(f"There are {even_count} even numbers in the list.")
''' 

'''
# Define the list of seven natural numbers
numbers = [1, 2, 3, 4, 5, 6, 7]

# Initialize variables to store the product of even numbers and the count of odd numbers
product_of_even_numbers = 1
odd_count = 0

# Iterate through the numbers
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        product_of_even_numbers *= num  # Multiply even numbers together
    else:
        odd_count += 1  # Increment the count of odd numbers

# Print the product of even numbers and the count of odd numbers
print(f"The product of even numbers is {product_of_even_numbers}")
print(f"There are {odd_count} odd numbers in the list.")
'''

'''
# Define the list of 10 natural numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Initialize variables to store the product of even numbers, the product of odd numbers, and the counts of even and odd numbers
product_of_even_numbers = 1
product_of_odd_numbers = 1
even_count = 0
odd_count = 0

# Iterate through the numbers
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        product_of_even_numbers *= num  # Multiply even numbers together
        even_count += 1  # Increment the count of even numbers
    else:
        product_of_odd_numbers *= num  # Multiply odd numbers together
        odd_count += 1  # Increment the count of odd numbers

# Print the results
print(f"The product of even numbers is {product_of_even_numbers}")
print(f"The count of even numbers is {even_count}")
print(f"The product of odd numbers is {product_of_odd_numbers}")
print(f"The count of odd numbers is {odd_count}")
'''
# Define the list of positive and negative integers
numbers = [-10, 5, -8, 7, -6, 2, -3, 9, -4, 1, -2, 6, -7, 3, -5, 4, -1, 8, -9, 10, -11]

# Initialize variables to store the product of even numbers, the product of odd numbers, and the counts of even and odd numbers
product_of_even_numbers = 1
product_of_odd_numbers = 1
even_count = 0
odd_count = 0

# Iterate through the numbers
for num in numbers:
    if num % 2 == 0:  # Check if the number is even
        product_of_even_numbers *= num  # Multiply even numbers together
        even_count += 1  # Increment the count of even numbers
    else:
        product_of_odd_numbers *= num  # Multiply odd numbers together
        odd_count += 1  # Increment the count of odd numbers

# Print the results
print(f"The product of even numbers is {product_of_even_numbers}")
print(f"The count of even numbers is {even_count}")
print(f"The product of odd numbers is {product_of_odd_numbers}")
print(f"The count of odd numbers is {odd_count}")