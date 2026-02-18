# Break Example
numbers = [1, 3, 7, 12, 8, 15]
target = 12

print("Searching for:", target)

for number in numbers:
    if number == target:
        print("Found:", number)
        break
    print("Checked:", number)

# Continue Example
print("\nEven numbers only:")
even_sum = 0

for num in range(1, 11):
    if num % 2 != 0:
        continue
    even_sum += num
    print("Processing:", num)

print("Sum of even numbers:", even_sum)
