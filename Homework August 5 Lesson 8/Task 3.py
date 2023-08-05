def make_operation(operator, *numbers):
    if operator == '+':
        result = sum(numbers)
    elif operator == '-':
        result = numbers[0]
        for number in numbers[1:]:
            result -= number
    elif operator == '*':
        result = numbers[0]
        for number in numbers[1:]:
            result *= number
    else:
        result = 'Incorrect operator inserted'
    return result


print(make_operation('*', 2, 5, 3))
print(make_operation('+', 50, 6, 20, 108))
