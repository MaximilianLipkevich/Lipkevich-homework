import random

# task1
generatedNumber = random.randint(1, 10)
userNumber = int(input("Enter your number:\n")) # also isdigit check can be used

if generatedNumber == userNumber:
    print("Congrats! You guessed the number correctly!")
else:
    print(f"The correct number was {generatedNumber}. You lost.")
#ok


# task2
name = input("What is your name?\n")
age = int(input("What is your age?\n"))

print(f"Hello {name.capitalize()}, on your next birthday you’ll be {age + 1} years old.")
#ok

# task3
string = input("Enter your sentence:\n")
def shuffleLetters(string):
    stringLetters = [i for i in string]
    stringIndexes = [i for i in range(0, len(stringLetters))]
    random.shuffle(stringIndexes)
    result = ''
    for n in stringIndexes:
        result += string[n]
    return result

print(shuffleLetters(string), shuffleLetters(string), shuffleLetters(string), shuffleLetters(string), shuffleLetters(string))
#+