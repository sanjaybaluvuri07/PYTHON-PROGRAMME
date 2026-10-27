
balance = 5000
transactions = []

while True:
    print("\n===== ATM MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > 50000:
            print("Deposit limit is Rs. 50,000.")
        else:
            balance += amount
            transactions.append(f"Deposited: Rs. {amount:.2f}")
            print("Deposit successful!")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount!")
        elif amount > 10000:
            print("Withdrawal limit is Rs. 10,000.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions.append(f"Withdrawn: Rs. {amount:.2f}")
            print("Withdrawal successful!")

    elif choice == "3":
        print(f"Current Balance: Rs. {balance:.2f}")

    elif choice == "4":
        print("\n--- Transaction Summary ---")
        if len(transactions) == 0:
            print("No transactions yet.")
        else:
            for transaction in transactions:
                print(transaction)

        print(f"Available Balance: Rs. {balance:.2f}")

    elif choice == "5":
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Please select 1 to 5.")
