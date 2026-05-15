transactions = []

def add_income():
    amount = float(input("Enter income amount: "))
    description = input("Enter income description: ")
    transaction_type = "Income"
    transactions.append({"type": transaction_type, "amount": amount, "description": description})
    print("Income added successfully!")

def add_expense():
    amount = float(input("Enter expense amount: "))
    description = input("Enter expense description: ")
    transaction_type = "Expense"
    transactions.append({"type": transaction_type, "amount": amount, "description": description})
    print("Expense added successfully!")

def show_balance():
    balance = 0
    for transaction in transactions:
        if transaction['type'] == "Income":
            balance += transaction['amount']
        elif transaction['type'] == "Expense":
            balance -= transaction['amount']

    print(f"Current Balance: {balance}")

def show_transactions():
    if not transactions:
        print("No transactions recorded.")
        return

    for transaction in transactions:
        print(f"{transaction['type']}: {transaction['amount']} - {transaction['description']}")

def main():
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Show Balance")
        print("4. Show Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_income()
        elif choice == '2':
            add_expense()
        elif choice == '3':
            show_balance()
        elif choice == '4':
            show_transactions()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()