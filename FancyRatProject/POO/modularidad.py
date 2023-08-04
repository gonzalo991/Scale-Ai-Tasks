def add(a, b):
    """Función para sumar dos números."""
    return a + b

def subtract(a, b):
    """Función para restar dos números."""
    return a - b

def multiply(a, b):
    """Función para multiplicar dos números."""
    return a * b

def divide(a, b):
    """Función para dividir dos números."""
    if b != 0:
        return a / b
    else:
        raise ValueError("Cannot divide by zero.")

# Ejemplo de uso de las funciones
num1 = 10
num2 = 5

result1 = add(num1, num2)
result2 = subtract(num1, num2)
result3 = multiply(num1, num2)
result4 = divide(num1, num2)

print(f"Resultado suma: {result1}")
print(f"Resultado resta: {result2}")
print(f"Resultado multiplicación: {result3}")
print(f"Resultado división: {result4}")
