import pickle

def save_data(balance, transactions):
    with open("data.pkl", "wb") as f:
        data = {"balance": balance, "transactions": transactions}
        pickle.dump(data, f)

def load_data():
    try:
        with open("data.pkl", "rb") as f:
            data = pickle.load(f)
            return data["balance"], data["transactions"]
    except FileNotFoundError:
        return 0, []

def manage_balance():
    balance, transactions = load_data()
    balance_list = [balance]
    
    while True:
        print("1. Add Transaction")
        print("2. Show Balance")
        print("3. Show Transactions")
        print("4. Save Data")
        print("5. Quit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            transaction = float(input("Enter transaction amount: "))
            transactions.append(transaction)
            balance += transaction
            balance_list.append(balance)
            print(f"Transaction of {transaction} added successfully.")
        elif choice == 2:
            print(f"Your current balance is {balance}.")
        elif choice == 3:
            print("Transaction History:")
            for i in range(len(transactions)):
                print(f"{i+1}. {transactions[i]}")
            print(f"\nCurrent Balance: {balance}")
        elif choice == 4:
            save_data(balance, transactions)
            print("Data saved successfully.")
        elif choice == 5:
            save_data(balance, transactions)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
    
manage_balance()

