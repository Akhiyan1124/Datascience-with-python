# conditional_comprehensions.py

print("=== Conditional List Comprehension ===")

numbers = list(range(1, 21))

# Label numbers as Even or Odd
labels = ["Even" if num % 2 == 0 else "Odd" for num in numbers]

result = list(zip(numbers, labels))

print("Number Labels:")
for item in result:
    print(item)
