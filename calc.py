# Intro to Python Assignment: Basic Calculator Program

"""
This program simulates a basic calculator.
It asks the user for two numbers and a mathematical operation
(+, -, *, /) and then displays the result.
It includes basic error handling for invalid input and division by zero.
"""

print("--- Welcome to the Basic Python Calculator ---")

# --- Get User Input ---
# It's good practice to inform the user what you need.

# Prompt for the first number
num1_str = input("Enter the first number: ")

# Prompt for the second number
num2_str = input("Enter the second number: ")

# Prompt for the operation
# Remind the user of the valid options.
operation = input("Enter the operation you want to perform (+, -, *, /): ")


# --- Process and Calculate ---
# Use a try-except block to gracefully handle errors if the user enters
# non-numeric input where numbers are expected.
try:
    # Convert the input strings to floating-point numbers.
    # Using float allows for calculations with decimal numbers.
    num1 = float(num1_str)
    num2 = float(num2_str)

    result = None  # Initialize the result variable to None.
                   # This helps track if a valid calculation was performed.

    # Perform the calculation based on the operation symbol provided.
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        # Crucial Check: Prevent division by zero error.
        if num2 == 0:
            print("\nError: Division by zero is not mathematically allowed.")
            # Keep result as None since the operation is invalid.
        else:
            # Perform division only if the divisor is not zero.
            result = num1 / num2
    else:
        # Handle cases where the user entered an unsupported operation symbol.
        print(f"\nError: Invalid operation symbol '{operation}'. Please use one of: +, -, *, /")
        # Keep result as None.

    # --- Display Result ---
    # Only print the formatted result if a calculation was successfully completed
    # (i.e., result is no longer None).
    if result is not None:
        # Use an f-string for clean and readable output formatting.
        print(f"\nCalculation: {num1} {operation} {num2} = {result}")

except ValueError:
    # This 'except' block catches errors if float() fails.
    # This typically happens if the user types text (e.g., "five") instead of a number.
    print("\nError: Invalid number input. Please make sure you enter numeric values for both numbers.")

# Indicate the program has finished its attempt.
print("\n--- Calculator finished ---")
