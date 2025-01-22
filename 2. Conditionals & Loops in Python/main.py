# Step 1: If-Else Statements – Decision Making

# Checking if savings are positive or negative
savings = float(input("Enter your monthly savings: "))

if savings > 0:
    print("Great! You are saving money")
elif savings == 0:
    print("You are breaking even")
else:
    print("Warning! You are spending more than you earn.")

# Task 1
# Write a program that asks for a user's income and expenses, then:
# Prints "You are making a profit!" if income > expenses.
# Prints "You are breaking even." if income == expenses.
# Prints "You are in loss!" if income < expenses.

monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your monthly expenses: "))

if monthly_income > monthly_expenses:
    print("You are making a profit!")
elif monthly_income == monthly_expenses:
    print("You are breaking even.")
else:
    print("You are in loss!")

# Step 2: Loops – Automating Tasks

# For Loop (Fixed Repetitions)
# Print monthly savings for 6 months
for month in range(1, 7):
    print(f"Month {month}: You saved ${200}")

# While Loop (Unknown Repetitions)
# Count months until savings reach $1000
savings = 0
months = 0

while savings < 1000:
    savings += 200          # Saving $200 per month
    months += 1
    print(f"After {months} months, savings: {savings}")

# Task 1
# Write a program that:
# 1. Asks the user for their monthly savings goal.
# 2. Uses a while loop to simulate saving $300 per month until the goal is reached.
# 3. Prints how many months it took to reach the goal.

monthly_savings_goal = float(input("Enter your monthly savings goal: "))
total_saving = 0
total_months = 0

while total_saving <= monthly_savings_goal:
    total_saving += 300
    total_months += 1
    print(f"Month {total_months}: Savings = ${total_saving}")

print(f"For {total_saving}, it took {total_months} months")