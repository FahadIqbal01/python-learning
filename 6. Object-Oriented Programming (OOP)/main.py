# Step 1: Understanding Classes & Objects

# Creating a bank account class
class BankAccount:
    def __init__(self, account_holder, balance= 0):
        self.account_holder = account_holder
        self.balance = balance

account1 = BankAccount(account_holder= "Alice", balance= 5000)
account2 = BankAccount(account_holder= "Bob", balance= 3000)

print(f"{account1.account_holder} has a balance of {account1.balance}")
print(f"{account2.account_holder} has a balance of {account2.balance}")

# Task 1: Create a Class for an Investment Account
# Define a class InvestmentAccount with:

# account_name (e.g., "Retirement Fund")
# balance (default = 0)
# Create two investment accounts and print their names & balances.

class InvestmentAccount:
    def __init__(self, account_name, balance = 0):
        self.account_name = account_name
        self.balance = balance

account1 = InvestmentAccount(account_name= "Retirement Fund", balance= 7000)
account2 = InvestmentAccount(account_name= "CDC Fund", balance= 10000)

print(f"{account1.account_name} has a balance of {account1.balance}")
print(f"{account2.account_name} has a balance of {account2.balance}")

#  Step 2: Adding Methods (Functions inside a Class)

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposite ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient fund")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")


account1 = BankAccount(account_holder= "Alice", balance= 5000)

account1.deposit(amount= 1000)
account1.withdraw(amount= 2000)
account1.withdraw(amount= 5000)

# Task 2: Add Deposit & Withdraw Methods to InvestmentAccount
# Add a deposit() method that increases the balance.
# Add a withdraw() method that prevents withdrawing more than the balance.
# Test with different deposit and withdrawal amounts.

class InvestmentAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")


account1 = InvestmentAccount(account_holder= "Fahad", balance= 20000)

account1.deposit(amount= 25000)
account1.withdraw(amount= 9500)
account1.withdraw(amount= 50000)

# Step 3: Inheritance (Reusing Classes)
# Example: Creating a Savings Account from BankAccount

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposite ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient fund")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate= 0.05):
        super().__init__(account_holder, balance)       # inherit_attributes
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added: ${interest}. New balance: ${self.balance}")

savings = SavingsAccount(account_holder= "5000", balance= 5000)

savings.deposit(amount= 1000)
savings.add_interest()

# Task 3: Create a RetirementAccount Class (Inheriting from InvestmentAccount)
# The class should inherit from InvestmentAccount.
# Add an interest_rate attribute.
# Add a method to apply interest to the balance.
# Create an object and test it.

class InvestmentAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")

class RetirementAccount(InvestmentAccount):
    def __init__(self, account_holder, balance=0, interest_rate= 0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest added ${interest}. New balance: ${self.balance}")

retirementAccount1 = RetirementAccount(account_holder= "Fahad", balance= 5000000)

retirementAccount1.add_interest()

