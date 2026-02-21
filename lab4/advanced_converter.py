def convert_from_celsius(celsius):
    try:
        celsius = float(celsius)

        if celsius < -273.15:
            return None, None, None, "Below absolute zero"

        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        rankine = (celsius + 273.15) * 9/5

        return fahrenheit, kelvin, rankine, "Success"

    except ValueError:
        return None, None, None, "Invalid input"


if __name__ == "__main__":
    f, k, r, status = convert_from_celsius(100)

    if status == "Success":
        print("100°C conversions:")
        print("Fahrenheit:", f)
        print("Kelvin:", k)
        print("Rankine:", r)
    else:
        print("Error:", status)
