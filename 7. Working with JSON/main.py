import json

# 1. Converting Python objects to JSON (Serialization)

# Python dictionary
data = [
    ("Income", 50000, "January's salary", "Salary"),
    ("Expense", 25000, "Monthly house rent", "Rent")
]

# Convert python dictionary to JSON object
json_string = json.dumps(obj= data)
print(json_string)

# 2. Parsing JSON into Python objects (Deserialization)
json_string = '{"name" : "John", "age" : 30, "city" : "New York"}'

data = json.loads(s= json_string)
print(data)

# 3. Reading JSON from a file
# Read JSON from a file
with open(file= "data.json", mode= "r") as file:
    data = json.load(fp= file)
    print(data)

# 4. Writing JSON to a file
# Python data
data = {
    "name" : "John",
    "age" : 30,
    "city" : "New York"
}

# Write Python object to a JSON file
with open(file= "data.json", mode= "w") as file:
    json.dump(obj= data, fp=file, indent= 4)