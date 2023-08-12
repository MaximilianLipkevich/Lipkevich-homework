def count_lines(name):
    f = open(name)
    lines = f.readlines()
    print(len(lines))
    f.close()

def count_chars(name):
    f = open(name)
    string_a = f.read()
    print(len(string_a))
    f.close()

def test(name):
    count_lines(name)
    count_chars(name)