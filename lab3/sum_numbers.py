```python
# Sum Numbers Using For Loop

def calculate_sum():
    numbers = []
    print("Enter numbers to sum (type 'done' to finish)")

    while True:
        user_input = input("Enter number: ")

        if user_input.lower() == 'done':
            break

        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid number.")

    total = 0
    for num in numbers:
        total += num

    if numbers:
        print(f"Numbers: {numbers}")
        print(f"Total Sum: {total}")
        print(f"Average: {total / len(numbers):.2f}")
    else:
        print("No numbers entered.")

if __name__ == "__main__":
    calculate_sum()
