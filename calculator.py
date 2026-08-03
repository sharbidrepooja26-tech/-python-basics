# Simple Calculator Program
def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero!")
            return
    else:
        print("Invalid operator!")
        return
    
    print(f"Result: {num1} {operator} {num2} = {result}")

calculator()
