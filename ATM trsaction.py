
print("ATM TRANSACTION SYSTEM")
balance = 5000
deposits = 0
withdrawals = 0
rejected = 0
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            balance = balance + amount
            deposits = deposits + amount
            print("Deposit successful")
        else:
            print("Invalid amount")
            rejected = rejected + 1
    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Invalid amount")
            rejected = rejected + 1
        elif amount > 3000:
            print("Withdrawal limit exceeded")
            rejected = rejected + 1
        elif amount > balance:
            print("Insufficient balance")
            rejected = rejected + 1
        else:
            balance = balance - amount
            withdrawals = withdrawals + amount
            print("Withdrawal successful")
    elif choice == 0:
        break
    else:
        print("Invalid choice")
        rejected = rejected + 1
print("\nTRANSACTION SUMMARY")
print("Total Deposits:", deposits)
print("Total Withdrawals:", withdrawals)
print("Rejected Transactions:", rejected)
print("Final Balance:", balance)
