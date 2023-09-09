# Define a dictionary of workers with their information
workers = {
    'John': {'worked_hours': 45, 'weekly_payment': None},
    'Mary': {'worked_hours': None, 'weekly_payment': 800},
    'Peter': {'worked_hours': 30, 'weekly_payment': None},
    'Ana': {'worked_hours': None, 'weekly_payment': 600},
    'Louis': {'worked_hours': 50, 'weekly_payment': None},
}

# Define constants for the pay rate per hour and regular payment limit
PAY_PER_HOUR = 150
REGULAR_PAYMENT = 35 * PAY_PER_HOUR

# Iterate through the workers and their data
for worker, data in workers.items():
    # Access the 'worked_hours' and 'weekly_payment' values from the data dictionary
    worked_hours = data['worked_hours']
    weekly_payment = data['weekly_payment']
    
    # Initialize variables for rounded worked hours and rounded weekly payment
    rounded_worked_hours = None
    rounded_weekly_payment = None
    
    # Check if 'worked_hours' is not None
    if worked_hours is not None:
        # Calculate and round the worked hours to the nearest whole number
        rounded_worked_hours = round(worked_hours)
        
        # Calculate the payment based on rounded worked hours
        if rounded_worked_hours <= 35:
            rounded_weekly_payment = rounded_worked_hours * PAY_PER_HOUR
        else:
            regular_payment = 35 * PAY_PER_HOUR
            overtime_payment = (rounded_worked_hours - 35) * 1.5 * PAY_PER_HOUR
            rounded_weekly_payment = regular_payment + overtime_payment
    
    # Check if 'weekly_payment' is not None
    elif weekly_payment is not None:
        # Calculate and round the worked hours based on the weekly payment
        if weekly_payment > REGULAR_PAYMENT:
            overtime_payment = weekly_payment - REGULAR_PAYMENT
            overtime_hours = overtime_payment / (1.5 * PAY_PER_HOUR)
            rounded_worked_hours = round(35 + overtime_hours)
        elif weekly_payment <= REGULAR_PAYMENT:
            rounded_worked_hours = round(weekly_payment / PAY_PER_HOUR)
        
        # Assign the weekly payment value
        rounded_weekly_payment = round(weekly_payment)
    
    # Print the results with rounded values
    print(f"The worked hours for {worker} is: {rounded_worked_hours} hours")
    print(f"The payment for {worker} is: ${rounded_weekly_payment}")
