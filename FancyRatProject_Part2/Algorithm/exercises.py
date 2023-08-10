subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]
print("The subjects of the course are:")
for subject in subjects:
    print(subject)

# ----------------------------------------------------------------

def ellipse_area(a, b, pi):
    area = pi * a * b
    return area

a = 6
b = 12
pi = 3.14
area = ellipse_area(a, b, pi)
print("The area of the ellipse is: " + str(area))

# ----------------------------------------------------------------

def calculate_invoice_total(amount, vat_percentage):
    if not vat_percentage:
        vat_percentage = 21
    total = amount + (amount * vat_percentage / 100)
    return total

amount = 100
vat_percentage = None
total = calculate_invoice_total(amount, vat_percentage)
print("The total of the invoice is: " + str(total))

# ---------------------------------------------------------------- 
import math

# Function to calculate the area of a circle and the volume of a cylinder.
def circle_area_and_cylinder_volume(**kwargs):
    # Check if both height and radius are provided.
    if kwargs.get('height') and kwargs.get('radius'):
        radius = float(kwargs.get('radius'))  # Convert radius to a floating-point number.
        height = kwargs.get('height')
        
        # Calculate the area of the circle's base.
        basearea = math.pi * radius ** 2
        
        # Calculate the volume of the cylinder by multiplying the base area by the height.
        volume = basearea * height
        return volume
    
    # Check if only the radius is provided (no height).
    elif kwargs.get('radius') and not kwargs.get('height'):
        radius = float(kwargs.get('radius'))  # Convert radius to a floating-point number.
        area = math.pi * radius ** 2  # Calculate the area of the circle.
        return area
    
    # If no valid parameters are provided, print an error message.
    else:
        print('Invalid parameters')

# Example usage
circle_radius = 5
cylinder_radius = 4
cylinder_height = 10

# Calculate the area of the circle using the circle_area_and_cylinder_volume() function.
circle_area_result = circle_area_and_cylinder_volume(radius=circle_radius)

# Calculate the volume of the cylinder using the circle_area_and_cylinder_volume() function.
cylinder_volume_result = circle_area_and_cylinder_volume(radius=cylinder_radius, height=cylinder_height)

# Print the results.
print("Area of the circle:", circle_area_result)
print("Volume of the cylinder:", cylinder_volume_result)

# ----------------------------------------------------------------

def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print("The average of the numbers is: " + str(average))
