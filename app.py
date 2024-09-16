import datetime

# Initialize an empty dictionary for expense tracking
expenses = {}

# Function to add an expense
def add_expense(category, amount):
    date = datetime.date.today()
    # Ensure the category exists in the dictionary, or create it
    if category not in expenses:
        expenses[category] = []
    # Append the amount and date to the respective category
    expenses[category].append({"amount": amount, "date": date})
    print(f"Added {amount} to {category} on {date}.")

# Function to view all expenses
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    print("Expenses by category:")
    for category, exp_list in expenses.items():
        print(f"\nCategory: {category}")
        for exp in exp_list:
            print(f"  - {exp['amount']} on {exp['date']}")

# Function to get a summary of total expenses
def get_summary():
    total_expenses = 0
    category_summary = {}
    
    for category, exp_list in expenses.items():
        category_total = sum(exp["amount"] for exp in exp_list)
        category_summary[category] = category_total
        total_expenses += category_total

    print("\nExpense Summary:")
    print(f"Total Expenses: {total_expenses}")
    print("Category Breakdown:")
    for category, total in category_summary.items():
        print(f"  - {category}: {total}")

# Main loop for user interaction
def main():
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. Get summary")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            add_expense(category, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            get_summary()
        elif choice == '4':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
