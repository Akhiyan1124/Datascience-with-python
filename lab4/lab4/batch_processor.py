def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def process_temperature_list(temps):
    results = []
    for temp in temps:
        try:
            temp = float(temp)
            converted = celsius_to_fahrenheit(temp)
            results.append((temp, converted))
        except ValueError:
            print("Skipping invalid:", temp)
    return results


if __name__ == "__main__":
    temperatures = [0, 25, 37, 100]
    results = process_temperature_list(temperatures)

    for original, converted in results:
        print(f"{original}°C → {converted:.2f}°F")
