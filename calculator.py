# Basic Calulator Program
num1 = float(input("Enter the first nymber: "))
num2 = float(input("Enter the second number: "))

operation = input ("Chose an operation (+, -, *, /): ")
#Perform the operation and print the result
if operation == '+':
    result = num1+num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 -num2
    print(f"{num1} -{num2} = {result}")
elif operation == '*':
    result = num1*num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print (f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else: 
    print("Invalid operation. Please choose +, -, *, or /.")
    