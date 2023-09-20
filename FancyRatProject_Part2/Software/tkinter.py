import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector

class EmployeeManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Manager")

        # Initialize database connection
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='root',
            database='employees_db'
        )

        self.cursor = self.conn.cursor()

        # Create and layout GUI widgets
        self.create_widgets()

    def add_employee(self):
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        department = self.department_entry.get()
        hire_date = self.hire_date_entry.get()
        salary_entry_text = self.salary_entry.get()

        try:
            salary = float(salary_entry_text)
        except ValueError:
            self.status_label.config(text="Invalid salary value")
            return

        # Insert the employee data into the database
        insert_query = "INSERT INTO employees (first_name, last_name, email, department, hire_date, salary) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(insert_query, (name, last_name, email, department, hire_date, salary))
        self.conn.commit()

        # Clear the entry fields after adding an employee
        self.name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.department_entry.delete(0, tk.END)
        self.hire_date.delete(0,tk.END)
        self.salary_entry.delete(0, tk.END)
        self.status_label.config(text="Employee added successfully")

    def create_widgets(self):
        # Labels and Entry fields
        ttk.Label(self.root, text="Name:").grid(row=0, column=0)
        ttk.Label(self.root, text="Last Name:").grid(row=1, column=0)
        ttk.Label(self.root, text="Email: ").grid(row=2, column=0)
        ttk.Label(self.root, text="Department:").grid(row=3, column=0)
        ttk.Label(self.root, text="Hire Date:").grid(row=4, column=0)
        ttk.Label(self.root, text="Salary:").grid(row=5, column=0)

        self.name_entry = ttk.Entry(self.root)
        self.last_name_entry = ttk.Entry(self.root)
        self.email_entry = ttk.Entry(self.root)
        self.department_entry = ttk.Entry(self.root)
        self.hire_date_entry = ttk.Entry(self.root)
        self.salary_entry = ttk.Entry(self.root)

        self.name_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.email_entry.grid(row=2, column=1)
        self.department_entry.grid(row=3, column=1)
        self.hire_date_entry.grid(row=4, column=1)
        self.salary_entry.grid(row=5, column=1)

        # Buttons
        ttk.Button(self.root, text="Add Employee", command=self.add_employee).grid(row=6, column=0)
        ttk.Button(self.root, text="Exit", command=self.exit_program).grid(row=6, column=1)

        # Status label
        self.status_label = ttk.Label(self.root, text="")
        self.status_label.grid(row=5, columnspan=2)

    def exit_program(self):
        self.conn.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeManager(root)
    root.mainloop()