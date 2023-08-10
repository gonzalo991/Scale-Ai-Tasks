def filter_list(boolean_function, list):
    '''
    Function that receives a boolean function and a list and returns a new list with the elements that return True when the boolean function is applied to them.
    Parameters:
        boolean_function: A function that takes an element of the list and returns a boolean value.
        list: A list with elements to be filtered.
    Returns:
        A new list with the elements that return True when the boolean function is applied to them.
    '''
    new_list = []
    for element in list:
        if boolean_function(element):
            new_list.append(element)
    return new_list

def is_positive(num):
    '''
    Function that returns True if the number is positive, False otherwise.
    '''
    return num > 0

# Example of usage:
list = [1, -1, 2, -2, 3, -3]

filtered_list = filter_list(is_positive, list)

print(filtered_list)