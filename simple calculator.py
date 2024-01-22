def calculator(x,y,op):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        return "unknown value"
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"
    else:
        return "unknown value"