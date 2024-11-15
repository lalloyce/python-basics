def convert_temperature():
    # Print welcome message
    print("Welcome to the Temperature Converter!")
    print("Options: C for Celsius, F for Fahrenheit, K for Kelvin")

    # Get input from user
    from_scale = input("Enter the scale you're converting from (C/F/K): ").upper()
    to_scale = input("Enter the scale you're converting to (C/F/K): ").upper()

    # Check if the scales are valid
    valid_scales = ['C', 'F', 'K']
    if from_scale not in valid_scales or to_scale not in valid_scales:
        print("Invalid scale. Please enter C, F, or K.")
        return

    # Get temperature from user
    try:
        temperature = float(input(f"Enter the temperature in {from_scale}: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    # Check if temperature is above absolute zero
    if from_scale == 'C' and temperature < -273.15:
        print("Error: Temperature cannot be below -273.15°C (absolute zero)")
        return
    elif from_scale == 'F' and temperature < -459.67:
        print("Error: Temperature cannot be below -459.67°F (absolute zero)")
        return
    elif from_scale == 'K' and temperature < 0:
        print("Error: Temperature cannot be below 0K (absolute zero)")
        return

    # If converting to same scale, no conversion needed
    if from_scale == to_scale:
        print(f"The temperature is {temperature} {to_scale}")
        return

    # Convert the temperature
    converted_temp = 0

    # Convert from Celsius
    if from_scale == 'C':
        if to_scale == 'F':
            # Formula: °F = (°C × 9/5) + 32
            converted_temp = (temperature * 9/5) + 32
        else:  # to Kelvin
            # Formula: K = °C + 273.15
            converted_temp = temperature + 273.15

    # Convert from Fahrenheit
    elif from_scale == 'F':
        if to_scale == 'C':
            # Formula: °C = (°F - 32) × 5/9
            converted_temp = (temperature - 32) * 5/9
        else:  # to Kelvin
            # Formula: K = (°F - 32) × 5/9 + 273.15
            converted_temp = (temperature - 32) * 5/9 + 273.15

    # Convert from Kelvin
    elif from_scale == 'K':
        if to_scale == 'C':
            # Formula: °C = K - 273.15
            converted_temp = temperature - 273.15
        else:  # to Fahrenheit
            # Formula: °F = (K - 273.15) × 9/5 + 32
            converted_temp = (temperature - 273.15) * 9/5 + 32

    # Print the result
    print(f"The temperature in {to_scale} is {converted_temp:.2f} {to_scale}")

# Run the program
convert_temperature()