# Import Flask, request, and psycopg2 libraries
from flask import Flask, jsonify, request
import psycopg2
from psycopg2 import OperationalError, IntegrityError  # Import specific exceptions for database errors

# Create a Flask app instance
app = Flask(__name__)

# Database configuration dictionary
db_config = {
    'dbname': 'your_db_name',      # Replace with your actual database name
    'user': 'your_db_user',        # Replace with your actual database user
    'password': 'your_db_password',  # Replace with your actual database password
    'host': 'localhost',           # Replace with your actual database host or IP
    'port': '5432'                # Replace with your actual database port
}

# Function to establish a new connection to the database for each request
def connect_to_database():
    try:
        conn = psycopg2.connect(**db_config)
        return conn
    except OperationalError as e:
        print(f"OperationalError: {e}")
        return None

# Define a Flask route to retrieve a list of customers
@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # Establish a new database connection for this request
        conn = connect_to_database()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        # Use 'with' statement for managing the cursor
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()

        # Prepare customer data as a list of dictionaries
        customer_list = []
        for customer in customers:
            customer_dict = {
                "id": customer[0],
                "name": customer[1],
                "email": customer[2]
            }
            customer_list.append(customer_dict)

        # Return the list of customers as JSON
        return jsonify(customer_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()  # Close the database connection in a finally block

# Define a Flask route to add a customer
@app.route('/customers', methods=['POST'])
def add_customer():
    try:
        # Establish a new database connection for this request
        conn = connect_to_database()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        # Get customer data from the request's JSON body
        customer_data = request.get_json()

        # Check if the customer with the same email already exists
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE email = %s", (customer_data['email'],))
            existing_customer = cursor.fetchone()

            if existing_customer is None:
                # Prepare the SQL query to add a new customer
                sql = "INSERT INTO customers (name, email) VALUES (%s, %s)"
                params = (customer_data['name'], customer_data['email'])

                # Execute the SQL query to add a new customer
                cursor.execute(sql, params)
                conn.commit()  # Commit the transaction

                # Return the status of the operation as JSON
                return jsonify({"status": "Customer added successfully"})
            else:
                return jsonify({"error": "Customer with the same email already exists"}), 400
    except IntegrityError as e:
        return jsonify({"error": "IntegrityError: Database constraint violation"}), 400
    except OperationalError as e:
        return jsonify({"error": f"OperationalError: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()  # Close the database connection in a finally block

# Define a Flask route to delete a customer
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        # Establish a new database connection for this request
        conn = connect_to_database()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        # Prepare the SQL query to delete a customer
        sql = "DELETE FROM customers WHERE id = %s"
        params = (customer_id, )

        # Execute the SQL query to delete a customer
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            conn.commit() # Commit the transaction

            # Return the status of the operation as JSON
            return jsonify({"status": "Customer deleted successfully"})
    except IntegrityError as e:
        return jsonify({"error": "IntegrityError: Database constraint violation"}), 400
    except OperationalError as e:
        return jsonify({"error": f"OperationalError: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close() # Close the database connection in a finally block

# Function to validate customer data
def validate_customer_data(customer_data):
    if 'name' not in customer_data or 'email' not in customer_data:
        return False
    if not isinstance(customer_data['name'], str) or not isinstance(customer_data['email'], str):
        return False
    return True

# Define a Flask route to update a customer
@app.route('/customers/<int:customer_id>', methods=['PATCH'])
def update_customer(customer_id):
    try:
        # Establish a new database connection for this request
        conn = connect_to_database()
        if conn is None:
            return jsonify({"error": "Failed to connect to the database"}), 500

        # Get customer data from the request's JSON body
        customer_data = request.get_json()

        # Validate customer data
        if not validate_customer_data(customer_data):
            return jsonify({"error": "Invalid customer data"}), 400

        # Check if the customer with the same ID exists
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            existing_customer = cursor.fetchone()

            if existing_customer is None:
                return jsonify({"error": "Customer not found"}), 404
            else:
                # Prepare the SQL query to update a customer
                sql = "UPDATE customers SET name = %s, email = %s WHERE id = %s"
                params = (customer_data['name'], customer_data['email'], customer_id)

                # Execute the SQL query to update a customer
                cursor.execute(sql, params)
                conn.commit()  # Commit the transaction

                # Return the status of the operation as JSON
                return jsonify({"status": "Customer updated successfully"})
    except IntegrityError as e:
        return jsonify({"error": "IntegrityError: Database constraint violation"}), 400
    except OperationalError as e:
        return jsonify({"error": f"OperationalError: {e}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()  # Close the database connection in a finally block

# Run the Flask app if this script is executed directly
if __name__ == "__main__":
    app.run(debug=True)

