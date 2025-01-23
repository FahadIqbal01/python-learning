# Step 1: Writing to a File
# Writing financial data to a file
with open("finance_report.txt", "w") as file:
    file.write("January: $5000\n")
    file.write("February: $5200\n")
    file.write("March: $4800\n")

print("Data written to file successfully")

# Task 1:
# Create a file called expenses.txt.
# Write 3 months of expense data into it.
# Print "Expenses saved successfully." when done.

with open("expenses.txt", "w") as file:
    file.write("April : $5200\n")
    file.write("May : $3650\n")
    file.write("June : $4850\n")

print("Expenses saved successfully")

# Step 2: Reading from a File

# Reading from a file
with open("finance_report.txt", "r") as file:
    content = file.read()

print("File content:\n", content)

# Task 2:
# Read the expenses.txt file created in Task 1.
# Print all the expense data on the screen.

with open("expenses.txt", "r") as file:
    content = file.read()

print("File content:\n", content)

# Step 3: Appending Data to a File

# Appending new data to the file
with open("finance_report.txt", "a") as file:
    file.write("April: $5300\n")

# print("New data added to the file")

# Task 3:
# Append a 4th month’s expense to expenses.txt.
# Print "New expense added." after updating the file.

with open("expenses.txt", "a") as file:
    file.write("July : $3250\n")

print("New expense added")

# Step 4: Working with CSV Files (Financial Data)

# import csv

# Writing to a CSV file
with open(file= "transactions.csv", mode= "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Type", "Amount"])
    writer.writerow(["2024-01-01", "Income", 5000])
    writer.writerow(["2024-01-05", "Expense", -2000])

print("CSV file created successfully")

# Task 4:
# Create a CSV file called budget.csv.
# Add columns: Month, Income, Expenses, Savings.
# Write data for 3 months.

import csv

with open(file= "budget.csv", mode= "w", newline= "") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Income", "Expenses", "Savings"])
    writer.writerow(["January", 5000, 2000, 3000])
    writer.writerow(["February", 5200, 2200, 3000])
    writer.writerow(["March", 4800, 2100, 2700])