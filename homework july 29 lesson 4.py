import math
import random

# task1
string = input("Enter the string:\n")

if len(string) < 2:
    result = ''
else:
    result = string[0] + string[1] + string[-2] + string[-1]

print(result)
#ok


# task2
phoneNumber = input("Enter the phone number:\n")

if not phoneNumber.isdigit(): #nice check)
    print("The number should only contain digits in it.")
else:
    print("The number is made out of digits.")

if len(phoneNumber) > 10 or len(phoneNumber) < 10: # You can use == and 'not' orerators for this check) 
    print("The number should contain 10 digits.")
else:
    print("The amount of digits is correct.")



# task3
a = random.randint(1, 99)
b = random.randint(1, 99)

addition = [a + b, f'{a} + {b}']
subtraction = [a - b, f'{a} - {b}']
multiplication = [a * b, f'{a} * {b}']
division = [a / b, f'{a} / {b}']

methods = (addition, subtraction, multiplication, division)
chosenMethod = methods[random.randint(0, 3)]

mathQuestion = int(input(f"What is the result of {chosenMethod[1]} ?\n"))

if chosenMethod[0] == mathQuestion:
    print("Your answer is correct")
else:
    print(f"Your answer is incorrect. The correct answer is {chosenMethod[0]}")
# very good but a little bic complicated as for the first lessons. But still ok)


# task4
myname = "maximilian"
askedName = input("What is your name?\n")
result = None

if askedName.lower() == myname:
    result = True
else:
    result = False

print(result)

#+