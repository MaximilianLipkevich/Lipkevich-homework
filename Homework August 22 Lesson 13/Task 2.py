def added_number(x):
    def add_to(y):
        return x + y
    return add_to

add_five = added_number(5)

result = add_five(3)
print(result)