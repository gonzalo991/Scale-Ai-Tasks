import mysql.connector

# Connection to the database
def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="airline"
        )

        if connection.is_connected():
            print("Connection to the database established")
            return connection
        else:
            raise Exception("Database connection failed")

    except mysql.connector.Error as e:
        print(f"MySQL Error during database connection: {e}")
        raise
    except Exception as e:
        print(f"An error occurred during database connection: {e}")
        raise

# Check if the "flight_reservations" table exists and create it if necessary
def create_flight_reservations_table(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS flight_reservations (
                    reservation_id INT AUTO_INCREMENT PRIMARY KEY,
                    flight_id INT,
                    passenger_id INT,
                    price DECIMAL(10, 2),
                    date DATE,
                    FOREIGN KEY (flight_id) REFERENCES flights(flight_id) ON DELETE CASCADE,
                    FOREIGN KEY (passenger_id) REFERENCES passengers(passenger_id) ON DELETE CASCADE
                )
            """)

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        raise

# Create a connection to the MySQL database and save a reservation
def save_reservation(flight_id, passenger_id, price, date):
    try:
        # Establish a connection to the MySQL database
        connection = create_connection()

        # Create the "flight_reservations" table if it doesn't exist
        create_flight_reservations_table(connection)

        with connection.cursor() as cursor:
            # Insert the new reservation into the database
            cursor.execute("INSERT INTO flight_reservations (flight_id, passenger_id, price, date) VALUES (%s, %s, %s, %s)",
                           (flight_id, passenger_id, price, date))
            connection.commit()

        print("Reservation saved successfully!")

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
    except Exception as error:
        print("An error occurred:", error)
    finally:
        # Close the connection in a finally block to ensure it's always closed
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create a connection to the MySQL database and edit a reservation
def edit_reservation(reservation_id, new_price, new_date):
    try:
        # Establish a connection to the MySQL database
        connection = create_connection()

        # Create the "flight_reservations" table if it doesn't exist
        create_flight_reservations_table(connection)

        with connection.cursor() as cursor:
            # Update the reservation with the new price and date
            cursor.execute("UPDATE flight_reservations SET price = %s, date = %s WHERE reservation_id = %s",
                           (new_price, new_date, reservation_id))
            affected_rows = cursor.rowcount  # Check the number of affected rows
            connection.commit()

            if affected_rows > 0:
                print("Reservation edited successfully!")
            else:
                print(f"No reservation found with ID {reservation_id}. No changes were made.")

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
    except Exception as error:
        print("An error occurred:", error)
    finally:
        # Close the connection in a finally block to ensure it's always closed
        if connection.is_connected():
            cursor.close()
            connection.close()

# Example usage
flight_id = 1
passenger_id = 2
price = 500.00
date = "2023-09-17"
save_reservation(flight_id, passenger_id, price, date)

reservation_id = 3
new_price = 550.00
new_date = "2023-09-18"
edit_reservation(reservation_id, new_price, new_date)