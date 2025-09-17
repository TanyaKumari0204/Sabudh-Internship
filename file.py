# Custom exception class for negative numbers
class NegativeNumberError(Exception):
    def __init__(self, value):
        super().__init__(f"NegativeNumberError: Negative number entered: {value}")

# Main program to divide two numbers with error handling
try:
    # Prompt user for input
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Raise custom exception if any number is negative
    if num1 < 0:
        raise NegativeNumberError(num1)
    if num2 < 0:
        raise NegativeNumberError(num2)

    # Perform division
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except NegativeNumberError as e:
    print(e)

except ValueError:
    print("Error: Invalid input. Please enter integers only.")

else:
    print(f"Result: {result}")

finally:
    print("Program execution completed.")

# ---------------------------------------------------------------
# Brief Write-Up of Findings

# ● How does the try-except block handle the ZeroDivisionError?
#   The try block attempts to divide two numbers. If the second number is zero,
#   Python raises a ZeroDivisionError. The except block catches this and prints
#   a clear error message instead of crashing the program.

# ● What happens when the NegativeNumberError is raised?
#   If either input number is negative, the program raises a custom exception
#   called NegativeNumberError. This is caught and handled gracefully with a
#   descriptive message showing the invalid value.

# ● How does using custom exceptions improve the error handling in your program?
#   Custom exceptions allow for more specific and readable error handling.
#   They help distinguish different types of input errors and make the code
#   easier to maintain and extend.

# ● What did you learn about error and exception handling in Python from this assignment?
#   I learned how to use try-except-else-finally blocks effectively, how to catch
#   built-in exceptions like ZeroDivisionError and ValueError, and how to define
#   and raise custom exceptions. This improves program reliability and user experience.
