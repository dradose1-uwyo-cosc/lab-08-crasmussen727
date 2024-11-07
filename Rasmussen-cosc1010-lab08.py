# Calvin Rasmussen
# UWYO COSC 1010
# Submission Date
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: notes from class.
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_to_number(s):
    try:
        # Try to convert to int first
        return int(s)
    except ValueError:
        try:
            # If not an int, try to convert to float
            if s.count('.') == 1 and s.replace('.', '', 1).isdigit():  # Check if it's a valid float with one decimal point
                return float(s)
            else:
                return False
        except ValueError:
            return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
def slope_intercept(m, b, x_lower, x_upper):
    # Check if the bounds are integers
    if not isinstance(x_lower, int) or not isinstance(x_upper, int):
        return False
    
    # Ensure lower bound is less than or equal to upper bound
    if x_lower > x_upper:
        return False

    y_values = []
    for x in range(x_lower, x_upper + 1):
        y = m * x + b
        y_values.append(y)
    return y_values


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def user_input_slope_intercept():
    while True:
        m = input("Enter the slope (m), or type 'exit' to quit: ")
        if m.lower() == 'exit':
            break
        m = convert_to_number(m)
        if m is False:
            print("Invalid input for m. Please enter a valid number.")
            continue
        
        b = input("Enter the y-intercept (b): ")
        b = convert_to_number(b)
        if b is False:
            print("Invalid input for b. Please enter a valid number.")
            continue
        
        x_lower = input("Enter the lower bound for x: ")
        x_lower = convert_to_number(x_lower)
        if x_lower is False or not isinstance(x_lower, int):
            print("Invalid input for lower bound. Please enter an integer.")
            continue
        
        x_upper = input("Enter the upper bound for x: ")
        x_upper = convert_to_number(x_upper)
        if x_upper is False or not isinstance(x_upper, int):
            print("Invalid input for upper bound. Please enter an integer.")
            continue
        
        result = slope_intercept(m, b, x_lower, x_upper)
        if result is False:
            print("Invalid bounds or other input error. Please try again.")
        else:
            print(f"Computed y values: {result}")
            break
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
import math 

def square_root(n):
    if n < 0:
        return None
    return math.sqrt(n)

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4 * a * c
    sqrt_disc = square_root(discriminant)
    if sqrt_disc is None:
        return None  # No real solutions if discriminant is negative, instead would be imaginary 
    
    x1 = (-b + sqrt_disc) / (2 * a)
    x2 = (-b - sqrt_disc) / (2 * a)
    return (x1, x2)
def user_input_quadratic_formula():
    while True:
        a = input("Enter the coefficient a, or type 'exit' to quit: ")
        if a.lower() == 'exit':
            break
        a = convert_to_number(a)
        if a is False:
            print("Invalid input for a. Please enter a valid number.")
            continue
        
        b = input("Enter the coefficient b: ")
        b = convert_to_number(b)
        if b is False:
            print("Invalid input for b. Please enter a valid number.")
            continue
        
        c = input("Enter the coefficient c: ")
        c = convert_to_number(c)
        if c is False:
            print("Invalid input for c. Please enter a valid number.")
            continue
        
        result = quadratic_formula(a, b, c)
        if result is None:
            print("No real solutions exist.")
        else:
            print(f"Solutions: {result}")
            break
