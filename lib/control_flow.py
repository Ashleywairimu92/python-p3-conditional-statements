# control_flow.py

def admin_login(username, password):
    """Check if the provided username and password grant access."""
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    """Return a message based on the given temperature."""
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature < 65:
        return "It's a little chilly out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    else:  # temperature > 85
        return "It's too dang hot out there!"

def fizzbuzz(num):
    """Return 'Fizz', 'Buzz', 'FizzBuzz', or the number itself based on its divisibility."""
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    """Perform basic arithmetic operations based on the provided operator."""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return None  # Handle division by zero if needed
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
