# The code below shows how to store the account holder name and the current balance
# It explains how to add money to the balance
# It explains how to remove money if the balance is enough
# It prevents withdrawing more than the available balance
# You can use this structure in simple finance simulations or training projects

class BankAccount:
    def __init__(self, account_holder, balance=0):   # creates a new account with name and optional balance
        self.account_holder = account_holder         # saves account holder name
        self.balance = balance                       # saves balance

    def deposit(self, amount):                       # adds money
        self.balance += amount                       # increases balance
        print(f"Deposited {amount}. New balance: {self.balance}")  # prints new balance

    def withdraw(self, amount):                      # removes money
        if amount <= self.balance:                   # checks if balance is enough
            self.balance -= amount                   # decreases balance
            print(f"Withdrew {amount}. Remaining balance: {self.balance}")  # prints remaining balance
        else:
            print("Insufficient funds")              # prints not enough money message

# Example usage
account = BankAccount("Alice")      # creates a bank account object
account.deposit(1000)               # adds one thousand
account.withdraw(500)               # removes five hundred
account.withdraw(1000)              # tries to withdraw more than balance