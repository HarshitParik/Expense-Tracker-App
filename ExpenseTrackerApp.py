class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category, description):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print('Expense added successfully!')

    def view_expenses(self):
        if self.expenses:
            print('Expenses:')
            for index, expense in enumerate(self.expenses, 1):
                print(f'{index}. Amount: {expense.amount}, Category: {expense.category}, Description: {expense.description}')
        else:
            print('No expenses to display.')

    def calculate_total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f'Total expenses: {total}')

# Example usage
tracker = ExpenseTracker()

while True:
    print('Expense Tracker')
    print('1. Add Expense')
    print('2. View Expenses')
    print('3. Calculate Total Expenses')
    print('4. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        amount = float(input('Enter amount: '))
        category = input('Enter category: ')
        description = input('Enter description: ')
        tracker.add_expense(amount, category, description)
    elif choice == '2':
        tracker.view_expenses()
    elif choice == '3':
        tracker.calculate_total_expenses()
    elif choice == '4':
        print('Exiting...')
        break
    else:
        print('Invalid choice. Please try again.')
