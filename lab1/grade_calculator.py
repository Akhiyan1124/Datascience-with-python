# grade_calculator.py

name = input("Enter student name: ")
marks = float(input("Enter marks: "))

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

print("\nStudent Name:", name)
print("Marks:", marks)
print("Grade:", grade)
