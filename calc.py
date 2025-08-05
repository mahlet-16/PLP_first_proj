num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2    
elif operation == '*':  
    result = num1 * num2
elif operation == '/':      
    result = num1 / num2
else:
    result = "Invalid operation"

print(f"The result is: {result}")