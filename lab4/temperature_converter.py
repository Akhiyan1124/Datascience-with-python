
Paste this CLEAN version:

```python
# Basic Temperature Conversion Functions

def greet_user():
    print("Welcome to the Temperature Converter Lab!")
    print("Let's learn about functions together!\n")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


if __name__ == "__main__":
    greet_user()

    print("25°C =", celsius_to_fahrenheit(25), "°F")
    print("77°F =", round(fahrenheit_to_celsius(77), 2), "°C")
