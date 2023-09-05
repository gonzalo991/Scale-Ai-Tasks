from flask import Flask, request, jsonify
import psycopg2
from psycopg2 import extras
import os

app = Flask(__name__)

# Function to create a database connection
def create_connection():
    try:
        # Retrieve database credentials from environment variables
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_host = os.environ.get('DB_HOST')
        db_port = os.environ.get('DB_PORT')
        db_name = os.environ.get('DB_NAME')

        # Check if any of the required environment variables is missing
        if not all([db_user, db_password, db_host, db_port, db_name]):
            raise EnvironmentError("Database credentials are not properly configured")

        connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
            dbname=db_name
        )
        return connection
    except psycopg2.Error as error:
        # Raise an exception to indicate a database connection error
        raise EnvironmentError(f"Error while connecting to PostgreSQL: {error}")

@app.route('/', methods=['POST'])
def list_students():
    try:
        # Create a database connection
        with create_connection() as connection:
            # Create a cursor for executing queries
            with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
                # Execute the SQL query to select all students
                cursor.execute("SELECT * FROM students")
                # Fetch all rows as dictionaries
                rows = cursor.fetchall()
                # Return the query result as JSON
                return jsonify(rows)
    except EnvironmentError as e:
        # Handle database connection errors with a 500 Internal Server Error
        return jsonify(error=str(e)), 500
    except Exception as e:
        # Handle other exceptions with a 400 Bad Request
        return jsonify(error=str(e)), 400
    
    # New route to add a student
@app.route('/add_student', methods=['POST'])
def add_student():
    try:
        # Get student data from the request JSON
        student_data = request.get_json()

        # Validate incoming JSON data
        if not all(key in student_data for key in ['name', 'age', 'grade']):
            raise ValueError("Incomplete student data")

        # Create a database connection
        with create_connection() as connection:
        # Create a cursor for executing queries
            with connection.cursor() as cursor:
        # Execute the SQL query to insert a new student
                cursor.execute(
                "INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)",
                (student_data['name'], student_data['age'], student_data['grade'])
                )

            # Commit the transaction
                connection.commit()

                return jsonify(message="Student added successfully")
    except ValueError as e:
        # Handle validation errors with a 400 Bad Request
        return jsonify(error=str(e)), 400
    except EnvironmentError as e:
        # Handle database connection errors with a 500 Internal Server Error
        return jsonify(error=str(e)), 500
    except Exception as e:
        # Handle other exceptions with a 500 Internal Server Error
        return jsonify(error=str(e)), 500


# New route to update a student
@app.route('/update_student', methods=['POST'])
def update_student():
    try:
    # Get student data from the request JSON
        student_data = request.get_json()

    # Validate incoming JSON data
        if not all(key in student_data for key in ['id', 'name', 'age', 'grade']):
            raise ValueError("Incomplete student data")

    # Create a database connection
        with create_connection() as connection:
    # Create a cursor for executing queries
            with connection.cursor(cursor_factory=extras.RealDictCursor) as cursor:
    # Execute the SQL query to update a student
                cursor.execute(
                "UPDATE students SET name = %s, age = %s, grade = %s WHERE id = %s",
                (student_data['name'], student_data['age'], student_data['grade'], student_data['id'])
                )

    # Commit the transaction
                connection.commit()

                return jsonify(message="Student updated successfully")
    except ValueError as e:
    # Handle validation errors with a 400 Bad Request
        return jsonify(error=str(e)), 400
    except EnvironmentError as e:
    # Handle database connection errors with a 500 Internal Server Error
        return jsonify(error=str(e)), 500
    except Exception as e:
    # Handle other exceptions with a 500 Internal Server Error
        return jsonify(error=str(e)), 500

# New route to delete a student
@app.route('/delete_student', methods=['POST'])
def delete_student():
    try:
        # Get student id from the request JSON
        student_id = request.get_json()['id']

        # Create a database connection
        with create_connection() as connection:
            # Create a cursor for executing queries
            with connection.cursor() as cursor:
                # Execute the SQL query to delete a student using a parameterized query
                cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))

                # Commit the transaction
                connection.commit()

        return jsonify(message="Student deleted successfully")
    except EnvironmentError as e:
        # Handle database connection errors with a 500 Internal Server Error
        return jsonify(error=str(e)), 500
    except Exception as e:
        # Handle other exceptions with a 500 Internal Server Error
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run()