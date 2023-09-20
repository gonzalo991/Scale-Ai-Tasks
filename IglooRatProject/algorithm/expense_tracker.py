import csv
from datetime import datetime

# Initialize budget and expenses
budget = float(input("Enter your monthly budget: $"))
expenses = []

def save_expenses_to_csv(expense_data):
    try:
        with open("expenses.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Category", "Expense", "Amount", "Date"])
            writer.writerows(expense_data)
    except IOError as e:
        print(f"Error saving expenses to CSV: {e}")

def load_expenses_from_csv():
    try:
        with open("expenses.csv", mode="r") as file:
            reader = csv.DictReader(file)
            return [(row["Category"], row["Expense"], float(row["Amount"]), row["Date"]) for row in reader]
    except FileNotFoundError:
        return []
    except IOError as e:
        print(f"Error loading expenses from CSV: {e}")
        return []

expenses = load_expenses_from_csv()

while True:
    # Display menu options
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Budget and Savings")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    try:
        if choice == '1':
            # Add expense
            category = input("Enter the category of the expense: ")
            expense_name = input("Enter the name of the expense: ")
            expense_amount = float(input("Enter the expense amount: $"))
            expense_date = input("Enter the date (YYYY-MM-DD, or leave empty for today): ")

            if not expense_date:
                expense_date = datetime.now().strftime("%Y-%m-%d")

            expenses.append((category, expense_name, expense_amount, expense_date))
            print(f"Expense '{expense_name}' added successfully!")

            # Save expenses to CSV file
            save_expenses_to_csv(expenses)

        elif choice == '2':
            # View expenses
            print("\nExpense List:")
            for category, name, amount, date in expenses:
                print(f"Category: {category}, Expense: {name}, Amount: ${amount:.2f}, Date: {date}")

        elif choice == '3':
            # View budget and savings
            total_expenses = sum(amount for _, _, amount, _ in expenses)
            savings = budget - total_expenses
            print(f"\nBudget: ${budget:.2f}")
            print(f"Total Expenses: ${total_expenses:.2f}")
            print(f"Savings: ${savings:.2f}")

        elif choice == '4':
            # Exit the program
            print("Exiting Expense Tracker. Have a nice day!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

    except ValueError as e:
        print(f"ValueError: {e}. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")
