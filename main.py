# Celsius to Fahrenheit
def celsius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

# Celsius to Kelvin
def celsius_to_kelvin(celcius):
    return celcius + 273

# Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Fahrenheit to Kelvin
def fahrenheit_to_kelvin(fahrenheit):
    celcius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celcius)

# Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273

# Kelvin to Fahrenheit
def kelvin_to_fahrenheit(kelvin):
    celcius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celcius)



# main function
def main():
    try:
        value = float(input('Enter the temperature value: '))
        unit = input('Enter the unit (Celsius, Fahrenheit, or Kelvin): ').strip().lower()
    except ValueError:
        return {'error': "Invalid temperature value. Please enter a valid number."}

    if unit == 'celsius':
        return {
            'Fahrenheit': f'{celsius_to_fahrenheit(value):.2f} F',
            'Kelvin': f'{celsius_to_kelvin(value):.2f} K'
        }
    elif unit == 'fahrenheit':
        return {
            'Celsius': f'{fahrenheit_to_celsius(value):.2f} C',
            'Kelvin': f'{fahrenheit_to_kelvin(value):.2f} K'
        }
    elif unit == 'kelvin':
        if value < 0:
            return {'error': 'Kelvin temperature cannot be negative.'}
        return {
            'Celsius': f'{kelvin_to_celsius(value):.2f} C',
            'Fahrenheit': f'{kelvin_to_fahrenheit(value):.2f} F'
        }
    else:
        return { 'error': 'Invalid unit. Please enter a valid unit (Celsius, Fahrenheit, or Kelvin).'}
    

print('Result:', main())