def oops():
    list_a = [1, 2, 3, 4]
    return list_a[5]

try:
    oops()
except IndexError:
    print("You've caused an index error!")
