stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

choice = input('Enter the fruit stock you want to calculate,\ntype "all" if you want to calculate everything:\n')

whole_price = []
if choice == "all":
    for item in stock:
        whole_price.append(stock[item] * prices[item])
    print(sum(whole_price))
else:
    result = stock[choice] * prices[choice]
    print(result)
