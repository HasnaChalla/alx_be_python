FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temperature = float(input("Enter the temperature to convert: "))
temperature_unit = input(
    "Is this temperature in Celsius or Fahrenheit? (C/F):")


def convert_to_celsius(fahrenheit):
    fahrenheit = temperature * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature}°C is {fahrenheit}°F")
    return fahrenheit


def convert_to_fahrenheit(celsius):
    celsius = temperature * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    print(f"{temperature}°F is {celsius}°C")
    return celsius


if temperature_unit.upper() == "C":
    convert_to_fahrenheit(temperature)
elif temperature_unit.upper() == "F":
    convert_to_celsius(temperature)
