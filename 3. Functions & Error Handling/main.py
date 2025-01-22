# Step 1: Understanding Functions

# Function to calculate total savings
def calculate_savings(income, expenses):
    return income - expenses                 # Returns savings

# Using the function
monthly_income = float(input("Enter income: "))
monthly_expenses = float(input("Enter expenses: "))
savings = calculate_savings(income = monthly_income, expenses = monthly_expenses)

print(f'Your monthly savings: ${savings}')

# Task 1:
# Create a function that:
# Takes loan amount, interest rate, and years as input
# Returns the total amount to be paid after interest

def calculate_total_amount(loan_amount, interest_rate, years):
    return loan_amount * (1 + interest_rate * years)

loan = float(input("Enter loan amount: "))
rate = float(input("Enter interest rate: "))
years = float(input("Enter number of years: "))
total_amount = calculate_total_amount(loan_amount= loan, interest_rate= rate, years= years)

print(f"Total amount to be paid ${total_amount}")

# Step 2: Error Handling with Try-Except

try:
    amount = float(input("Enter an amount: "))
    print(f"You entered: ${amount}")
except ValueError:
    print(f"Invalid input! Please enter a number")

# Task 2:
# Write a program that:
# Asks for income and expenses
# Handles invalid input (e.g., user enters text instead of numbers)
# Prints the monthly savings

income = 0
expense = 0

try:
    income = float(input("Enter your income: "))
except ValueError:
    print('Invalid input! Please enter a number')
try:
    expense = float(input("Enter your expense: "))
except:
    print('Invalid input! Please enter a number')

monthly_savings = income - expense

print(f'Monthly savings: ${monthly_savings}')

# Step 3: Functions + Loops = Power!

def savings_growth(initial_savings, monthly_savings, months):
    for month in range(1, months + 1):
        initial_savings += monthly_savings
        print(f'Month {month}: Savings = ${initial_savings}')

savings_growth(initial_savings= 1000, monthly_savings= 200, months= 12)

# Task 3:
# Create a function that:
# Takes initial savings, monthly deposit, and interest rate
# Calculates and prints the savings growth for 12 months

# Function to calculate savings growth
def savings_growth(initial_savings, monthly_deposit, interest_rate):
    for month in range(1, 13):  # Loop for 12 months
        initial_savings = (initial_savings + monthly_deposit) * (1 + interest_rate)
        print(f"Month {month}: Savings = ${initial_savings:.2f}")

# Get user input
initial_savings = float(input("Enter initial savings: "))
monthly_deposit = float(input("Enter monthly deposit: "))
interest_rate = float(input("Enter interest rate (as decimal): "))

# Call function
savings_growth(initial_savings, monthly_deposit, interest_rate)