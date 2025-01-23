# Step 1: Lists – Storing Multiple Items

# List of monthly expenses
expenses = [1200, 1500, 1100, 1800, 2000]

# Accessing elements
print("First month's expense:", expenses[0])

# Modifying a list
expenses.append(1700)               # Add new expense
print("Updated expenses:", expenses)

# Total expenses
print("Total", sum(expenses))

# Task 1:
# Create a list of your monthly incomes for 6 months.
# Calculate and print the average income.
# Find the highest and lowest income using max() and min().

expenses = [1600, 2200, 1100, 580, 1800, 2050]

def calculate_average_income(_expenses):
    total_expenses = 0
    for expense in _expenses:
        total_expenses = total_expenses + expense
    average_income = total_expenses / len(_expenses)
    print(f"Average income: {average_income}")

calculate_average_income(expenses)

print(f"Maximum income: {max(expenses)}")
print(f"Minimum income: {min(expenses)}")

# Step 2: Tuples – Immutable Data

# Store fixed loan interest rates (cannot be modified)

interest_rates = (0.03, 0.05, 0.07)

print("Available interest rates:", interest_rates)
print("Lowest interest rates:", min(interest_rates))

# Task 2:
# Create a tuple containing 3 different loan interest rates.
# Print the highest and lowest interest rate.

interest_rates = (0.41, 0.26, 0.15)

print("Highest interes rate:", max(interest_rates))
print("Lowest interest rate:", min(interest_rates))

# Step 3: Dictionaries – Key-Value Pairs

# Dictionary storing financial data
finance_data = {
    "January" : 5000,
    "February" : 5200,
    "March" : 4800
}

# # Accessing values
print("February's income:", finance_data["February"])

# # Adding new data
finance_data["April"] = 5300
print("Updated finance data:", finance_data)

# Total income
print("Total income:", sum(finance_data.values()))

# Task 3:
# Create a dictionary storing 3 months of expenses.
# Add a new month's expense to the dictionary.
# Calculate and print the total expenses.

monthly_expenses = {
    "May" : 5200,
    "June" : 2550,
    "July" : 6200
}

monthly_expenses["August"] = 4750

print("Total expense:", sum(monthly_expenses.values()))

# Step 4: Sets – Unique Values

# Unique expense categories
expense_categories = {"Rent", "Food", "Transport", "Food", "Bills"}

print("Unique expense categories:", expense_categories)

# Task
# Create a set of investment types (e.g., "Stocks", "Real Estate", "Crypto").
# Try adding a duplicate investment and print the set.

investment_types = {"Stocks", "Real Estate", "Crypto"}
investment_types.add("Stocks")
investment_types.add("Real Estate")

print("Investment types", investment_types)
