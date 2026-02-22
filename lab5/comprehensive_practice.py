# comprehensive_practice.py

print("=== Comprehensive Practice ===")

students = {
    "Ali": 85,
    "Sara": 92,
    "John": 67,
    "Ayesha": 74,
    "David": 58
}

print("Original student marks:")
print(students)

# Extract students who passed (>= 70)
passed_students = {name: marks for name, marks in students.items() if marks >= 70}

print("\nStudents who passed:")
print(passed_students)

# Create grade labels
grades = {name: ("A" if marks >= 90 else
                 "B" if marks >= 80 else
                 "C" if marks >= 70 else
                 "F")
          for name, marks in students.items()}

print("\nStudent Grades:")
print(grades)
