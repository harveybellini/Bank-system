def main():
    name = input("Enter your name: ")
    balance = float(input("Enter your initial balance: "))
    account = BankAccount(name, balance)
    
    while True:
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Your current balance is:", account.check_balance())
        elif choice == 2:
            amount = float(input("Enter the amount you want to deposit: "))
            print("Your new balance is:", account.deposit(amount))
        elif choice == 3:
            amount = float(input("Enter the amount you want to withdraw: "))
            print("Your new balance is:", account.withdraw(amount))
        elif choice == 4:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
