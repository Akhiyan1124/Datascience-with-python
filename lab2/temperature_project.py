# temperature_project.py
# Advanced Temperature Categorization System

print("=== Temperature Categorization System ===")

try:
    temperature = float(input("Enter temperature in Celsius: "))

    if temperature < 0:
        category = "Freezing"
    elif 0 <= temperature < 10:
        category = "Very Cold"
    elif 10 <= temperature < 20:
        category = "Cold"
    elif 20 <= temperature < 30:
        category = "Normal"
    elif 30 <= temperature < 40:
        category = "Hot"
    else:
        category = "Very Hot"

    print("\nTemperature:", temperature, "°C")
    print("Category:", category)

except ValueError:
    print("Invalid input! Please enter a numeric value.")
