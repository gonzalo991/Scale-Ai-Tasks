numbers = [ -12, 52, -9, 21, -91, 121, -71, 54, -7, 65 ]

# Filter positive numbers
positive_numbers = [num for num in numbers if num > 0]

# Filter negative numbers
negative_numbers = [num for num in numbers if num < 0]

# Calculate the average of positive numbers
if positive_numbers:
    average_positive = sum(positive_numbers) / len(positive_numbers)
else:
    average_positive = None  # Set to None if there are no positive numbers

# Calculate the minimum of positive numbers
minimum_positive = min(positive_numbers) if positive_numbers else None  # Set to None if there are no positive numbers

# Calculate the average of negative numbers
if negative_numbers:
    average_negative = sum(negative_numbers) / len(negative_numbers)
else:
    average_negative = None  # Set to None if there are no negative numbers

# Calculate the minimum of negative numbers
minimum_negative = min(negative_numbers) if negative_numbers else None  # Set to None if there are no negative numbers

# Print the results
if average_positive is not None:
    print(f"The average of positive numbers is: {average_positive}")
else:
    print("There are no positive numbers in the list.")
if minimum_positive is not None:
    print(f"The minimum of positive numbers is: {minimum_positive}")
else:
    print("There are no positive numbers in the list.")
if average_negative is not None:
    print(f"The average of negative numbers is: {average_negative}")
else:
    print("There are no negative numbers in the list.")
if minimum_negative is not None:
    print(f"The minimum of negative numbers is: {minimum_negative}")
else:
    print("There are no negative numbers in the list.")