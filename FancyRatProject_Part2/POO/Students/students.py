import mysql.connector

# Class Student
class Student:
    # Dunder init method
    def __init__(self, name, last_name, phone, email):
        self._name = name
        self._last_name = last_name
        self._phone = phone
        self._email = email

    # Dunder str method
    def __str__(self) -> str:
        # Prints the details of the student
        return f"Student: [ Name: {self._name}, Last Name: {self._last_name}, Phone: {self._phone}, Email: {self._email} ]"

    # Getter and Setter methods for name attribute
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    # Getter and Setter method for last name attribute
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    # Getter and Setter method for phone attribute
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, phone):
        self._phone = phone

    # Getter and Setter methods for email attribute
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @staticmethod
    def list_students(conn): # List student method
        cursor = conn.cursor()  # Object to interact with the database
        query = "SELECT * FROM students"  # Query to select the list of students
        cursor.execute(query)  # Executes the query
        results = cursor.fetchall()  # Save the results in a list

        # Print the results using Student instances
        for row in results:
            student = Student(row[0], row[1], row[2], row[3])
            print(student)

    @staticmethod
    def add_student(conn, name, last_name, phone, email): # Add student method
        cursor = conn.cursor()  # Object to interact with the database
        query = f"INSERT INTO students (name, last_name, phone, email) VALUES ('{name}', '{last_name}', {phone}, '{email}')"  # Query to insert a new student
        cursor.execute(query)  # Executes the query
        conn.commit()  # Commits the changes to the database

    @staticmethod
    def update_student(conn, name, last_name, phone, email, id): # Update student method
        cursor = conn.cursor()  # Object to interact with the database
        query = f"UPDATE students SET name = '{name}', last_name = '{last_name}', phone = {phone}, email = '{email}' WHERE id = {id}"  # Query to update a student
        cursor.execute(query)  # Executes the query
        conn.commit()  # Commits the changes to the database

    @staticmethod
    def delete_student(conn, id): # Delete student method
        cursor = conn.cursor()  # Object to interact with the database
        query = f"DELETE FROM students WHERE id = {id}"  # Query to delete a student
        cursor.execute(query)  # Executes the query
        conn.commit()  # Commits the changes to the database

# Replace the values with your own database credentials
config = {
    "user": "your_database_user",
    "password": "your_database_password",
    "host": "localhost",
    "database": "students_database_name"
}

conn = mysql.connector.connect(**config)

try:
    # Call the add_student method to add a student to the database
    Student.add_student(conn, "John", "Doe", "555-1234", "johndoe@example.com")
    
    # Call the list_students method to retrieve and print student details
    Student.list_students(conn)

    # Call the update_student method to update a student's information
    Student.update_student(conn, "Jane", "Smith", "555-5678", "janesmith@example.com", 1)
    
    # Call the delete_student method to delete a student
    Student.delete_student(conn, 2)

except Exception as err:
    print(f"Error: {err}")

finally:
    Student.list_students(conn)
    conn.close()