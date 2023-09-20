# Import necessary modules
from datetime import datetime
import mysql.connector

# Function to create a connection to the database
def create_db_connection():
    """
    Creates a database connection with the specified parameters.
    
    Returns:
        The database connection object.
    """
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tasks_db"
    )

# Task class to represent individual tasks
class Task:
    def __init__(self, name, description, due_date, status="pending"):
        """
        Initializes a Task object with the provided attributes.

        Args:
            name (str): The name of the task.
            description (str): A description of the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
            status (str, optional): The status of the task (default is "pending").
        """
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status

# Function to add a task to the database
def add_task(name, description, due_date, status="pending"):
    """
    Adds a new task to the database.

    Args:
        name (str): The name of the task.
        description (str): A description of the task.
        due_date (str): The due date of the task in YYYY-MM-DD format.
        status (str, optional): The status of the task (default is "pending").
    
    Prints:
        A success message if the task is added successfully.
        An error message if an exception occurs during the process.
    """
    try:
        # Create a new Task instance
        new_task = Task(name, description, due_date, status)
        # Add the task to the database
        with create_db_connection() as conn:
            cursor = conn.cursor()
            query = "INSERT INTO tasks (name, description, due_date, status) VALUES (%s, %s, %s, %s)"
            values = (new_task.name, new_task.description, new_task.due_date, new_task.status)
            cursor.execute(query, values)
            conn.commit()
            print("Task added successfully!")

    except Exception as e:
        print(f"An error occurred while adding a task: {e}")

# Function to display tasks from the database
def display_tasks():
    """
    Displays the list of tasks from the database.

    Prints:
        Task details including ID, name, description, due date, and status.
        A success message if the list is displayed successfully.
        An error message if an exception occurs during the process.
    """
    try:
        with create_db_connection() as conn:
            cursor = conn.cursor()
            query = "SELECT id, name, description, due_date, status FROM tasks"
            cursor.execute(query)
            values = cursor.fetchall()

            if values:
                for task in values:
                    print(f"Task ID: {task[0]}, Name: {task[1]}, Description: {task[2]} Due Date: {task[3]}, Status: {task[4]}")
                print("The list was displayed successfully")
            else:
                raise Exception("The task list is empty")
    except Exception as e:
        print(f"An error occurred while displaying tasks: {e}")

# Function to delete a task from the database
def delete_task(id):
    """
    Deletes a task from the database based on its ID.

    Args:
        id (int): The ID of the task to be deleted.
    
    Prints:
        A success message if the task is deleted successfully.
        An error message if an exception occurs during the process.
    """
    try:
        with create_db_connection() as conn:
            cursor = conn.cursor()
            query = "DELETE FROM tasks WHERE id = %s"
            value = (id,)
            cursor.execute(query, value)
            conn.commit()
            print(f"Task with ID {id}, deleted successfully")
    except Exception as e:
        print(f"An error occurred while deleting a task: {e}")

# Function to update a task in the database
def update_task(values):
    """
    Updates a task in the database using a tuple of updated values.

    Args:
        values (tuple): A tuple containing updated task data in the format (name, description, due_date, status, id).
    
    Prints:
        A success message if the task is updated successfully.
        An error message if an exception occurs during the process.
    """
    try:
        with create_db_connection() as conn:
            cursor = conn.cursor()
            query = "UPDATE tasks SET name=%s, description=%s, due_date=%s, status=%s WHERE id = %s"
            cursor.execute(query, values)
            conn.commit()
            print(f"Task updated successfully")
    except Exception as e:
        print(f"An error occurred while updating a task: {e}")

# Entry point of the program
if __name__ == "__main__":
    # Add two tasks to the database and display the list of tasks
    data = ("Clean the house", "I have to clean the house on Monday", "2023-09-18", "Completed", 2)
    update_task(data)
    display_tasks()
