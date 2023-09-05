# Import necessary libraries
from flask import Flask, request, jsonify
import psycopg2

# Set up Flask application
app = Flask(__name__)

# Define a function to create a database connection
def get_db_connection():
    return psycopg2.connect(
        dbname='your_db_name',
        user='your_db_user',
        password='your_db_password',
        host='your_db_host',
        port='your_db_port'
    )

# Define a function to handle database errors
def handle_db_error(e):
    return jsonify({"error": str(e)})

# Define a function to execute a query and return the result
def execute_query(query, params=None):
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                if params:
                    cur.execute(query, params)
                else:
                    cur.execute(query)
                results = cur.fetchall()
                num_rows = cur.rowcount
                return results, num_rows

    except Exception as e:
        return handle_db_error(e)

# Route to create a new delivery
@app.route('/deliveries', methods=['POST'])
def create_delivery():
    data = request.json
    results, num_rows = execute_query("""
        INSERT INTO deliveries (order_id, customer_id, package_id, status, delivery_date, delivery_time, comments)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """, (
        data['order_id'],
        data['customer_id'],
        data['package_id'],
        data['status'],
        data['delivery_date'],
        data['delivery_time'],
        data['comments']
    ))

    return jsonify(results[0][0])

# Route to retrieve a delivery by ID
@app.route('/deliveries/<int:delivery_id>', methods=['GET'])
def get_delivery(delivery_id):
    results, num_rows = execute_query("""
        SELECT * FROM deliveries WHERE id = %s;
    """, (delivery_id,))

    if results:
        return jsonify({
            "id": results[0][0],
            "order_id": results[0][1],
            "customer_id": results[0][2],
            "package_id": results[0][3],
            "status": results[0][4],
            "delivery_date": results[0][5],
            "delivery_time": results[0][6],
            "comments": results[0][7]
        })
    else:
        return jsonify({"error": "Delivery not found"}), 404

# Route to update a delivery by ID
@app.route('/deliveries/<int:delivery_id>', methods=['PUT'])
def update_delivery(delivery_id):
    data = request.json
    results, num_rows = execute_query("""
        UPDATE deliveries
        SET order_id = %s, customer_id = %s, package_id = %s, status = %s,
            delivery_date = %s, delivery_time = %s, comments = %s
        WHERE id = %s;
    """, (
        data['order_id'],
        data['customer_id'],
        data['package_id'],
        data['status'],
        data['delivery_date'],
        data['delivery_time'],
        data['comments'],
        delivery_id
    ))

    return jsonify({"message": "Delivery updated successfully"})

# Route to delete a delivery by ID
@app.route('/deliveries/<int:delivery_id>', methods=['DELETE'])
def delete_delivery(delivery_id):
    results, num_rows = execute_query("""
        DELETE FROM deliveries WHERE id = %s;
    """, (delivery_id,))

    return jsonify({"message": "Delivery deleted successfully"})

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5001)