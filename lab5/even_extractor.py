# even_extractor.py

print("=== Even Number Extractor ===")

numbers = list(range(1, 21))

# Using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

print("Original numbers:")
print(numbers)

print("\nEven numbers:")
print(even_numbers)
