string = input("Enter your sentence:\n")
words = string.split()
dictionary = {}

for word in words:
        dictionary[word] = words.count(word)

print(dictionary)