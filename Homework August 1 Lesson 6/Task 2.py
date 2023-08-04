import random

list1 = []
list2 = []
i = 0

while i < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    i += 1

list3 = []
commonIndex = 0

while len(list1) > commonIndex:
    if list1[commonIndex] in list2:
        list3.append(list1[commonIndex])
        commonIndex += 1
    else:
        commonIndex += 1

print(f'First list is {list1}')
print(f'Second list is {list2}')
print(f'Common numbers are {list(set(list3))}')

# be sure that you use all functional that we learn in sesson. This task will be more easier if you will use sets