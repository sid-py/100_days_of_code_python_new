from calc_art import logo

print(logo)

# Calculator

# Addition
def add(n1,n2):
    return n1 + n2

# Subtraction
def sub(n1,n2):
    return n1 - n2

# Multiplication
def mult(n1,n2):
    return n1 * n2

# Division
def divi(n1,n2):
    return n1 / n2

# Defining a dictionary


operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": divi,
    }

num1 = float(input("Enter the first number: "))
# Looping through the dictionary
continue_calc = True
while continue_calc:
    num2 = float(input("Enter the next number: "))
    for i in operations:
        print(i)    
    operator = input("Choose the operation you want to perform: ") 
    calculation_function = operations[operator]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operator} {num2} = {answer}")
    num1 = answer
    more_cal = input("Do you want to continue (y/n)?: ")
    if more_cal == "n":
        continue_calc = False
    
