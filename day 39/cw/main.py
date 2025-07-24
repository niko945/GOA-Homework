def basic_op(operator, value1, value2):
    if operator == '+':
        return value1 + value2
    elif operator == '-':
        return value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        if value2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return value1 / value2
    else:
        raise ValueError(f"Unsupported operator: {operator}")