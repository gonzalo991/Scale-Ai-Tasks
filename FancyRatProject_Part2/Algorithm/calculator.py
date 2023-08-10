from math import sin, cos, tan, exp, log

def apply_function(f, n):
    '''
    Function that applies a function to integers from 1 to n.
    Parameters:
        f: A function that takes a real number and returns another.
        n: A positive integer.
    Returns:
        A dictionary with pairs i:f(i) for each integer value i from 1 to n.
    '''
    functions = {'sin': sin, 'cos': cos, 'tan': tan, 'exp': exp, 'log': log}
    result = {}
    for i in range(1, n + 1):
        result[i] = functions[f](i)
    return result

def calculator():
    '''
    Function that applies a user-selected function (sin, cos, tan, exp, or log) to the list of integers from 1 to n.
    Prints a table with the sequence of integers and the result of applying the entered function.
    '''
    f = input('Enter the function to apply (sin, cos, tan, exp, log): ')
    n = int(input('Enter a positive integer: '))
    print("Integer\tFunction Value")
    print("----------------------")
    for i, j in apply_function(f, n).items():
        print(i, '\t', j)
    return

calculator()
