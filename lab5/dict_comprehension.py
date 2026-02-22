# dict_comprehension.py

print("=== Dictionary Comprehension Example ===")

numbers = list(range(1, 11))

# Create dictionary of number and its square
squares = {num: num ** 2 for num in numbers}

print("Numbers:")
print(numbers)

print("\nSquares dictionary:")
print(squares)
