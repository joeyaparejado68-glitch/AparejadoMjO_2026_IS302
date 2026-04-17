# Create a BankAccount class
class BankAccount:
    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    # Method to withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    # Method to display balance
    def display_balance(self):
        print("Balance:", self.balance)

# Create an account object
account = BankAccount("Mj", 1000)

# Perform transactions
account.deposit(9000)
account.withdraw(2000)

# Display remaining balance
account.display_balance()