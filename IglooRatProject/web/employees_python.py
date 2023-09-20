# Import the mysql.connector module for MySQL database interaction
import mysql.connector
# Import database exceptions from mysql connector
from mysql.connector import DatabaseError, Error
import re  # Import the regular expressions module for email validation


# Define a function to establish a database connection
def database_connection():
    try:
        # Attempt to connect to the MySQL database with provided credentials
        conn = mysql.connector.connect(
            host="localhost",
            database="employees_db",
            user="root",
            password="root"
        )

        # Check if the connection was successful
        if conn is not None:
            return conn
        else:
            # Raise an exception if the connection fails
            raise DatabaseError("There was a problem connecting to the database")
    except DatabaseError as database_error:
        # Handle any database exceptions that might occur during the connection attempt
        print(f"Database error: {database_error}")

# Define a function to display employee data
def display_employees():
    try:
        # Connect to the MySQL database
        conn = database_connection()

        # Use a cursor to interact with the database
        with conn.cursor() as cursor:
            # Define an SQL query to retrieve employee data from the database
            query = "SELECT employee_id, first_name, last_name, email, department, hire_date, salary FROM employees"
            
            # Execute the SQL query
            cursor.execute(query)
            
            # Fetch all rows of employee data
            employees = cursor.fetchall()

            if employees:
                # Display employee data in the console if there are results
                for employee in employees:
                    print(f"Employee ID: {employee[0]}, Name: {employee[1]}, Surname: {employee[2]} Email: {employee[3]}, Department: {employee[4]}, Hire Date: {employee[5]}, Salary: {employee[6]}")
                print("The list was displayed successfully")
            else:
                # raise an exception if there are no employees in the database
                raise Error("The list of employees is empty")

    except Error as display_employees_error:
        # Handle any exceptions that might occur during the display process
        print(f"An error occurred when showing the list of employees: {display_employees_error}")
    
    finally:
        # Ensure the database connection is closed, regardless of success or failure
        conn.close()


# Define a function to display the main menu and manage user choices
def show_menu():
    while True:
        print("-------- Menu --------:")
        print("1. Display Employees")
        print("2. Add Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            # Call the display_employees function if the user selects option 1
            display_employees()
        elif choice == '2':
            # Call the add_employee function if the user selects option 2
            add_employee()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            # Exit the program if the user selects option 3
            print("Leaving the program")
            return False
        else:
            # Raise an exception message for invalid choices
            raise Exception("Invalid choice, please try again")
        
# Define a function to add an employee
def add_employee():
    try:
        # Connect to the MySQL database
        conn = database_connection()

        # Use a cursor to interact with the database
        with conn.cursor() as cursor:
            # Prompt the user for input for each employee attribute
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate email format using a regular expression
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                print("Invalid email format. Please enter a valid email address.")
                return  # Exit the function if email is invalid

            department = input("Enter department: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")

            # Validate hire date format using a regular expression
            date_pattern = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(date_pattern, hire_date):
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                return  # Exit the function if hire date is invalid

            while True:
                try:
                    salary = float(input("Enter salary: "))  # Convert salary to a float
                    break  # Exit the loop if salary input is valid
                except ValueError:
                    print("Invalid input for salary. Please enter a numeric value.")

            # Save the employee attributes in a tuple
            employee_values = (first_name, last_name, email, department, hire_date, salary)

            # Define an SQL query to add an employee to the database
            query = "INSERT INTO employees (first_name, last_name, email, department, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
            
            # Execute the SQL query to add the employee using the provided input
            cursor.execute(query, employee_values)

            conn.commit()

            # Fetch the last row ID of the inserted employee
            last_id = cursor.lastrowid

            # Display a success message in the console
            print(f"Employee added successfully with ID: {last_id}, \nEmployee Data: [ {employee_values}]")

    except Error as add_employee_error:
        # Handle any exceptions that might occur during the add process
        print(f"An error occurred when adding the employee: {add_employee_error}")
    
    finally:
        # Ensure the database connection is closed, regardless of success or failure
        conn.close()

def update_employee():
    try:
        # Connect to the MySQL database
        conn = database_connection()

        # Use a cursor to interact with the database
        with conn.cursor() as cursor:
            # Prompt the user for input for each employee attribute
            while True:
                try:
                    employee_id = int(input("Enter employee's id to modify data: "))
                    break
                except ValueError as e:
                    print(f"Invalid input for employee ID: {e}")
                
            
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")

            # Validate email format using a regular expression
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.match(email_pattern, email):
                print("Invalid email format. Please enter a valid email address.")
                return  # Exit the function if email is invalid

            department = input("Enter department: ")
            hire_date = input("Enter hire date (YYYY-MM-DD): ")

            # Validate hire date format using a regular expression
            date_pattern = r'^\d{4}-\d{2}-\d{2}$'
            if not re.match(date_pattern, hire_date):
                print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                return  # Exit the function if hire date is invalid

            while True:
                try:
                    salary = float(input("Enter salary: "))  # Convert salary to a float
                    break  # Exit the loop if salary input is valid
                except ValueError:
                    print("Invalid input for salary. Please enter a numeric value.")
            # Save the employee attributes in a tuple
            employee_new_values = (first_name, last_name, email, department, hire_date, salary, employee_id)

            # Define an SQL query to update an employee into the database
            query = "UPDATE employees SET first_name=%s, last_name=%s, email=%s, department=%s, hire_date=%s, salary=%s WHERE employee_id=%s"
            
            # Execute the SQL query to update the employee using the provided input
            cursor.execute(query, employee_new_values)

            conn.commit()

            # Display a success message in the console
            print(f"Successfully updated Employee with ID: {employee_id}, \nEmployee New Data: [ {employee_new_values}]")

    except Error as update_employee_error:
        # Handle any exceptions that might occur during the update process
        print(f"An error occurred when updating the employee: {update_employee_error}")
    
    finally:
        # Ensure the database connection is closed, regardless of success or failure
        conn.close()

# Define a function to delete an employee by ID
def delete_employee():
    try:
        # Connect to the MySQL database
        conn = database_connection()

        # Use a cursor to interact with the database
        with conn.cursor() as cursor:
            # Prompt the user for the employee's ID to be deleted
            while True:
                try:
                    employee_id = int(input("Enter employee's ID to delete: "))
                    break
                except ValueError as e:
                    print(f"Invalid input for employee ID: {e}")

            # Check if the employee ID exists in the database
            if not employee_exists(cursor, employee_id):
                print(f"Employee with ID {employee_id} does not exist.")
                return  # Exit the function if the employee doesn't exist

            # Define an SQL query to delete the employee by their ID
            query = "DELETE FROM employees WHERE employee_id = %s"

            # Execute the SQL query to delete the employee using the provided ID
            cursor.execute(query, (employee_id,))

            conn.commit()

            # Display a success message in the console
            print(f"Successfully deleted Employee with ID: {employee_id}")

    except Error as delete_employee_error:
        # Handle any exceptions that might occur during the delete process
        print(f"An error occurred when deleting the employee: {delete_employee_error}")

    finally:
        # Ensure the database connection is closed, regardless of success or failure
        conn.close()

# Check if an employee exists in the database by their ID
def employee_exists(cursor, employee_id):
    query = "SELECT COUNT(*) FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))
    result = cursor.fetchone()
    return result[0] > 0

# Entry point of the script
if __name__ == '__main__':
    # Call the show_menu function to start the program
    show_menu()