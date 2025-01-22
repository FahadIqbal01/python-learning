print("Hello, Finance & Business with Python")

# Step 1: Python as a Calculator

# Basic Arithmetic
print(5 + 3)
print(10 - 4)
print(6 * 7)
print(8 / 2)
print(10 % 3)

# Task 1
# The total amount for a loan of $5,000 at 3% annual interest for 2 years.
print(5000 * 0.03 * 2)

# Task 2
# Split a $1,000 bill equally among 4 friends.
print(1000 / 4)

# Step 2: Variables – Storing Data

# Storing Data in Variables
principal = 5000
interest_rate = 0.03
years = 2

# Calculating the total amount
total_amount = principal * (1 + interest_rate * years)
print("Total amount: ", total_amount)

# Task 1
# Create a variable to store your monthly expenses and calculate your annual expenses.
monthly_expenses = 20000
annual_expenses = monthly_expenses * 12
print("Annual Expenses: ", annual_expenses)

# Step 3: Input – Getting User Data

# Getting user input
name = input("Enter your name: ")
print("Welcome to python, " + name + "!")

# Task 1
# Write a program to ask the user for their monthly income and monthly expenses, then calculate their monthly savings.
monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your monthly expenses: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
print("Monthly savings are", monthly_savings)