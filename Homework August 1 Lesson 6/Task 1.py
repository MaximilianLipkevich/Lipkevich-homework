import random

randomNumbers = []
i = 0

while i < 20:
    randomNumbers.append(random.randint(0, 1000))
    i += 1

randomNumbersIndex = 0
biggestNumber = 0

while len(randomNumbers) > randomNumbersIndex:
    if randomNumbers[randomNumbersIndex] > biggestNumber:
        biggestNumber = randomNumbers[randomNumbersIndex]
        randomNumbersIndex += 1
    else:
        randomNumbersIndex += 1

print(randomNumbers)
print(f'The biggest number in the list is {biggestNumber}')