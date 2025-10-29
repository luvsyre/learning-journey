# Program 1: Temperature Converter (Fahrenheit to Celsius)
def fahrenheit_to_celsius(f_temp):
    """Converts a temperature from Fahrenheit to Celsius."""
    c = (f_temp - 32) * 5 / 9
    return c

# Example usage:
test_temp_f = 68
converted_temp = fahrenheit_to_celsius(test_temp_f)
print(f"{test_temp_f}°F is equal to {converted_temp:.2f}°C") 
# The :.2f ensures the output is formatted to two decimal places

# Program 2: Calculator (Basic Operators)
def basic_calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    # Use elif for the next conditions
    elif operator == "-": # <-- Don't forget the colon here!
        return num1 - num2
    elif operator == "*": # <-- And here!
        return num1 * num2
    elif operator == "/": # <-- And here!
        # Safety check: Prevent division by zero, which causes an error.
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        # Final else to catch any other invalid operator input
        return "Invalid operator"
    
    # Program 3: Simple Password Checker
    def is_password_secure(password):
    if len(password) > 8: # len(password) gets the number, and we check if it's > 8
        return True
    else:
        return False # If not greater than 8, it's not secure
    




    #
# day9_practice.py: Review Python basics: variables, data types, operators.
# Practice: Calculator, Temperature Converter, Password Checker. Use functions.
#

# ----------------------------------------------------------------------
# 1. Temperature Converter (Fahrenheit to Celsius)
#    Formula: C = (F - 32) * 5 / 9
# ----------------------------------------------------------------------
def fahrenheit_to_celsius(f_temp):
    """Converts a temperature from Fahrenheit to Celsius."""
    c = (f_temp - 32) * 5 / 9
    return c

# Example Usage
print("--- Temperature Converter ---")
test_temp_f = 77
celsius_result = fahrenheit_to_celsius(test_temp_f)
print(f"{test_temp_f}°F is equal to {celsius_result:.2f}°C")
print("-" * 30)


# ----------------------------------------------------------------------
# 2. Basic Calculator (Add, Subtract, Multiply, Divide)
# ----------------------------------------------------------------------
def basic_calculator(num1, num2, operator):
    """Performs basic math operations (+, -, *, /) on two numbers."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        # Check for division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    else:
        return "Invalid operator"

# Example Usage
print("--- Basic Calculator ---")
print(f"10 + 5 = {basic_calculator(10, 5, '+')}")
print(f"20 / 4 = {basic_calculator(20, 4, '/')}")
print(f"10 / 0 = {basic_calculator(10, 0, '/')}") # Testing error case
print("-" * 30)


# ----------------------------------------------------------------------
# 3. Simple Password Checker (Length > 8 characters?)
# ----------------------------------------------------------------------
def is_password_secure(password):
    """Checks if a password string is greater than 8 characters long."""
    if len(password) > 8:
        return True
    else:
        return False

# Example Usage
print("--- Password Checker ---")
pw1 = "MySecurePW123" # Length 13
pw2 = "short"        # Length 5
print(f"Password '{pw1}' secure? {is_password_secure(pw1)}")
print(f"Password '{pw2}' secure? {is_password_secure(pw2)}")
print("-" * 30)

