def temperature_converter_with_logging(temp, from_scale, to_scale):
    try:
        temp = float(temp)
        from_scale = from_scale.upper()
        to_scale = to_scale.upper()

        if from_scale == "C":
            celsius = temp
        elif from_scale == "F":
            celsius = (temp - 32) * 5/9
        elif from_scale == "K":
            celsius = temp - 273.15
        else:
            return None, False, "Invalid scale"

        if celsius < -273.15:
            return None, False, "Below absolute zero"

        if to_scale == "C":
            result = celsius
        elif to_scale == "F":
            result = (celsius * 9/5) + 32
        elif to_scale == "K":
            result = celsius + 273.15
        else:
            return None, False, "Invalid scale"

        return round(result, 2), True, "Success"

    except ValueError:
        return None, False, "Invalid temperature"


if __name__ == "__main__":
    result, success, message = temperature_converter_with_logging(25, "C", "F")

    if success:
        print("25°C =", result, "°F")
    else:
        print("Error:", message)
