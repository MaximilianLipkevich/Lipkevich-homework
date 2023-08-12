def square():
    a = int(input("Enter the first number:\n"))
    b = int(input("Enter the second number:\n"))
    return a**2 / b

try:
    print(square())
except ValueError:
    print("Entered values should be numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("No errors")
