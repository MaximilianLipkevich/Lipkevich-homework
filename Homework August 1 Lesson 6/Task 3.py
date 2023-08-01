numbers = list(range(1, 101))
index = 0
result = []

while len(numbers) > index:
    if numbers[index] % 7 == 0 and not numbers[index] % 5 == 0:
        result.append(numbers[index])
        index += 1
    else:
        index += 1

print(result)