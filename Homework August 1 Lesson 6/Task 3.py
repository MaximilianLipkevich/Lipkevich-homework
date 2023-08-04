numbers = list(range(1, 101)) # Nice!
index = 0
result = []

while len(numbers) > index:
    if numbers[index] % 7 == 0 and not numbers[index] % 5 == 0:
        result.append(numbers[index])
        index += 1 #this inde increment is present in both parts of if-else construction. You can move it outside this code. See example at the bottom of file
    else:
        index += 1



print(result)


# while len(numbers) > index:
#     if numbers[index] % 7 == 0 and not numbers[index] % 5 == 0:
#         result.append(numbers[index])
#     index += 1