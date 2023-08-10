import random

def randomList(length):
    result = []
    for i in range(length):
        result.append(random.randint(1, 101))
    return result

