#Implement a program that simulates a basic bank account using a BankAccount class

class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Account Holder: {self.holder_name}, Account Number: {self.account_number}, Balance: ${self.balance}")

# Example usage:
account_number = input("Enter account number: ")
holder_name = input("Enter account holder's name: ")
initial_balance = float(input("Enter initial balance: "))
account = BankAccount(account_number, holder_name, initial_balance)

while True:
    print("\nBank Account Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    elif choice == '3':
        account.display_balance()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
