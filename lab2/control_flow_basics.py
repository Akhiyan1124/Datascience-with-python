# control_flow_basics.py
# Demonstration of if, elif, else and logical operators

print("=== Control Flow Basics ===\n")

# Simple if-else example
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Grade system
marks = float(input("\nEnter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)

# Logical operators example
print("\n=== Logical Operators Example ===")

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Invalid credentials.")

# OR operator
number = int(input("\nEnter a number: "))

if number == 5 or number == 10:
    print("You entered a special number!")
else:
    print("Normal number.")

# NOT operator
is_logged_in = False

if not is_logged_in:
    print("User is not logged in.")
