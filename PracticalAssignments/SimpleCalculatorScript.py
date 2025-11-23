# +, -, *, / from user input

def calculator_1():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter first number: "))
        operator = str(input("Enter operation (sum, sub, mul, div): ".strip().lower()))

        operations = {
            "sum": a + b,
            "sub": a - b,
            "mul": a * b,
            "div": "Cannot div by zero" if b == 0 else a/b
        }
        return operations.get(operator, "Invalid operator")
    except ValueError:
        return "Invalid number entered"
    

print(calculator_1())