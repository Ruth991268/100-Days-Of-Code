# ### function with outputs

# def my_function():
#     result=3*3
#     return result
# print(my_function())


# first_name=input("Enter your first name: ")
# second_name=input("Enter your second name: ")
# def format_name():
#     return(f"{first_name.title()} {second_name.title()}")
# print(format_name())
# x=len("Angela" )
# #x is the output len is function and angle is the input   





# #  text after return not be exected
# #mutiple return 
# def format(first_name,second_name):
#      if first_name==""or second_name=="":
#           return"you didn't provide valid inputs"
#      return f"{first_name.title()} {second_name.title()}"
# print(format(input("Enter your first name: "), input("Enter your second name: ")))



# # ### Exercise: leap year
# def is_leap_year(year):
#   if year%4==0:
#     if year%100==0:
#       if year%400==0:
#         return  True
#       else:
#         return False    
#     else:
#         return True 
#   else:
#     return False 
# year=int(input("Enter a year: "))
# month=int(input("Enter a month: "))
# if month in [1, 3, 5, 7, 8, 10, 12]:
#     days = 31
# elif month in [4, 6, 9, 11]:
#     days = 30
# elif month == 2:
#     if is_leap_year(year):
#         days = 29
#     else:
#         days = 28
# result = is_leap_year(year)
# print(f"{year} is a leap year: {result} and it has {days} days in month {month}.")

# ### Exercise: leap year
# def is_leap_year(year):
#   if year%4==0:
#     if year%100==0:
#       if year%400==0:
#         return  True
#       else:
#         return False    
#     else: 
#         return True 
#   else:
#     return False 
# year=int(input("Enter a year: "))
# month=int(input("Enter a month: "))
# def days_in_month(year,month):
#"""takws a year and month and returns the number of days in that month"""
#    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
#    if  is_leap_year(year) and month == 2:
#        return f"{month} has 29 days"  
#    return f"{month} has {month_days[month-1]} days"      
# print(days_in_month(year, month))






#exercise calculator

logo = """
 _____________________
|  _________________  |
| | Pythonista      | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""
print(logo)

import os  # For clearing the screen (optional)
logo = """
 _____________________
|  _________________  |
| | Pythonista      | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

# Clear screen (optional, works on most terminals)
os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print("Welcome to the calculator!")

# Define operation functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2

# Get initial inputs
num1 = float(input("Enter your first number: "))  # Fixed typo in prompt
num2 = float(input("Enter your second number: "))
operation = input("Enter the operation you want to perform (+, -, *, /): ")

# Perform first operation and store result
if operation == "+":
    result = add(num1, num2)
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = subtract(num1, num2)
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = multiply(num1, num2)
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    result = divide(num1, num2)
    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation. Please try again.")
    

# Allow chaining with another number and operation
while True:
    choice = input("Do you want to continue with another operation? (yes/no): ").lower()
    if choice != 'yes':
        break

    num3 = float(input("Enter another number: "))
    operation = input("Enter another operation (+, -, *, /): ")

    # Use the previous result as the first number for the next operation
    if operation == "+":
        result = add(result, num3)
        print(f"{result - num3} + {num3} = {result}")
    elif operation == "-":
        result = subtract(result, num3)
        print(f"{result + num3} - {num3} = {result}")
    elif operation == "*":
        result = multiply(result, num3)
        print(f"{result / num3} * {num3} = {result}")
    elif operation == "/":
        result = divide(result, num3)
        print(f"{result * num3 if isinstance(result, float) else result} / {num3} = {result}")
    else:
        print("Invalid operation. Please try again.")