class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


# Create account
account = BankAccount(300)

# Transactions
account.deposit(200)
account.withdraw(150)

# Display balance
print("Balance:", account.get_balance())