def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return fahrenheit, kelvin
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return celsius, kelvin
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return celsius, fahrenheit
    else:
        return None, None

def main():
    print("Hey there! Welcome to my Temperature Converter!")
    while True:
        try:
            value = float(input("Enter the temperature you want to convert: "))
        except ValueError:
            print("Uh oh! That's not a number. Please try again.")
            continue

        unit = input("Cool! Now enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
        
        if unit not in ['C', 'F', 'K']:
            print("Hmm, that doesn't look right. Please enter 'C', 'F', or 'K'.")
            continue
        
        converted1, converted2 = convert_temperature(value, unit)
        
        if unit == 'C':
            print(f"\n{value}°C is equal to {converted1:.2f}°F and {converted2:.2f} K")
        elif unit == 'F':
            print(f"\n{value}°F is equal to {converted1:.2f}°C and {converted2:.2f} K")
        elif unit == 'K':
            print(f"\n{value} K is equal to {converted1:.2f}°C and {converted2:.2f}°F")
        
        another_conversion = input("\nWant to do another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            print("\nThanks for using my converter! Bye!")
            break

if __name__ == "__main__":
    main()
